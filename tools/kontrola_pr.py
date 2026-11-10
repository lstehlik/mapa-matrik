"""Kontrola pull requestu: python3 tools/kontrola_pr.py <base> <head> [autor]

Čte jen data (git show), kód z pull requestu nespouští. Výsledek:
  0 = jen přidání, smí se sloučit automaticky
  1 = chyba (formát), PR se neslučuje
  2 = potřeba člověka (mění nebo maže cizí data, mimo data/, podezřelý text, moc bodů)
"""
import json
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kontrola import check

MAX_POINTS = 200
MAX_TEXT = 300
LISTS = ("points", "notes", "sources", "places", "sections")
NAME = re.compile(r"\b([A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ][a-záčďéěíňóřšťúůýž]+)\s+([A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ][a-záčďéěíňóřšťúůýž]+)")
PLACE_WORDS = {"Dvůr", "Horní", "Dolní", "Nová", "Nové", "Nový", "Stará", "Staré", "Starý", "Malá", "Malé", "Malý",
               "Velká", "Velké", "Velký", "Ves", "Lhota", "Hora", "Hory", "Městec", "Svatý", "Svatá", "Sv"}


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def read(ref, path):
    try:
        return json.loads(git("show", f"{ref}:{path}"))
    except subprocess.CalledProcessError:
        return None


def key(item):
    return json.dumps(item, ensure_ascii=False, sort_keys=True)


def texts(vol, items):
    for p in items:
        if isinstance(p, dict):
            yield p.get("note")
        else:
            yield p


def suspicious(text, places):
    if text is None:
        return None
    text = str(text)
    if len(text) > MAX_TEXT:
        return f"text delší než {MAX_TEXT} znaků"
    if "@" in text or re.search(r"\d{3}[ -]?\d{3}[ -]?\d{3}", text):
        return "text vypadá jako kontakt"
    known = {w for p in places for w in p.split()} | PLACE_WORDS
    for m in NAME.finditer(text):
        if m.group(1) not in known and m.group(2) not in known:
            return f"možné jméno osoby: „{m.group(0)}“"
    return None


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    base, head = argv[1], argv[2]
    author = argv[3] if len(argv) > 3 else None
    errors, human, added = [], [], 0
    for line in git("diff", "--name-status", "--no-renames", f"{base}...{head}").splitlines():
        status, path = line.split("\t", 1)
        p = pathlib.PurePosixPath(path)
        if p.parts[0] != "data" or p.suffix != ".json" or len(p.parts) != 3:
            human.append(f"{path}: změna mimo data/<archiv>/<id>.json")
            continue
        if status == "D":
            human.append(f"{path}: smazaný soubor")
            continue
        new = read(head, path)
        if not isinstance(new, dict):
            errors.append(f"{path}: není platný JSON objekt")
            continue
        errors += [f"{path}: {e}" for e in check(p, new)]
        old = read(base, path) or {}
        for field, value in old.items():
            if field in LISTS:
                missing = {key(x) for x in value or []} - {key(x) for x in new.get(field) or []}
                if missing:
                    human.append(f"{path}: mění nebo maže {field} ({len(missing)}×)")
            elif new.get(field) != value:
                human.append(f"{path}: mění pole {field}")
        old_keys = {key(x) for x in old.get("points") or []}
        new_points = [x for x in new.get("points") or [] if key(x) not in old_keys]
        added += len(new_points)
        for pt in new_points:
            if author and pt.get("by") != author:
                human.append(f"{path}: bod sn. {pt.get('scan')} má by={pt.get('by')!r}, autor PR je {author}")
        new_items = [x for f in ("points", "notes", "sections") for x in new.get(f) or []
                     if key(x) not in {key(y) for y in old.get(f) or []}]
        for text in texts(new, new_items):
            reason = suspicious(text, new.get("places") or [])
            if reason:
                human.append(f"{path}: {reason}")
    if added > MAX_POINTS:
        human.append(f"přidává {added} bodů (víc než {MAX_POINTS})")
    for e in errors:
        print(f"CHYBA {e}")
    for h in human:
        print(f"KE KONTROLE {h}")
    print(f"přidaných bodů: {added}")
    if errors:
        return 1
    if human:
        return 2
    print("OK: jen přidání, lze sloučit automaticky")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
