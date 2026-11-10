"""Rozcestník z katalogu Porta fontium (SOA Plzeň):
python3 tools/katalog_pf.py <složka se stránkami> <kniha nebo začátek, např. kozlany-> … [--zapsat]
python3 tools/katalog_pf.py <složka se stránkami> --vse [--zapsat]

Pozor na práva: katalog je databáze chráněná zvláštním právem pořizovatele (§ 88–94 autorského zákona) a podle
podmínek Porta fontium (https://www.portafontium.eu/terms-of-use) se popisy smí užívat jen nevýdělečně s uvedením zdroje.
Bez souhlasu archivu převáděj jen knihy, se kterými skutečně pracuješ; --vse (celý katalog) až se souhlasem SOA Plzeň.

Vstup jsou uložené stránky výpisu matrik portálu
https://www.portafontium.eu/searching/register?search_api_views_fulltext_1=&page=<n> (40 knih na stránku).
Nástroj nic nestahuje – stránky ulož předem šetrně (1 za 10 s, rodokmen: tools/slusne.py).
Z každého řádku vznikne svazek bez orientačních bodů: signatura, fara, obce s jinými názvy (aliases), roky a druhy.
Bez --zapsat jen vypíše souhrn. U knih, které v data/ už jsou, jen doplní chybějící aliases.
"""
import datetime
import html
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kontrola import check
from mapa import DATA

ARCHIVE = "soa-plzen"
BASE = "https://www.portafontium.eu/register/soap-pn/"
SIGNS = {"*": "N", "oo": "O", "+": "Z", "*i": "iN", "ooi": "iO", "+i": "iZ"}


def text(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment)).replace("\xa0", " ")).strip()


def cell(row, name):
    m = re.search(rf'<td[^>]*views-field-{name}[^>]*>(.*?)</td>', row, re.S)
    return m.group(1) if m else ""


def place(item):
    """„Kožlany (Koschlan, Kozlany)“ -> ("Kožlany", ["Koschlan", "Kozlany"])."""
    item = re.sub(r"\s*\[[^\]]*\]", "", item).strip()
    m = re.match(r"^(.*?)\s*\((.*)\)$", item)
    if not m:
        return item, []
    alts = [a.strip() for a in m.group(2).split(",") if a.strip() and a.strip() != m.group(1)]
    return m.group(1), alts


def records(fragment, unknown):
    spans = {}
    for div in re.findall(r"<div[^>]*>(.*?)</div>", fragment, re.S) or [fragment]:
        m = re.match(r"^(\d{4})(?:-(\d{4}))?\s*(.*)$", text(div))
        if not m:
            continue
        lo, hi = int(m.group(1)), int(m.group(2) or m.group(1))
        for sign in re.split(r"[,\s]+", m.group(3)):
            kind = SIGNS.get(sign)
            if not kind:
                if sign:
                    unknown[sign] = unknown.get(sign, 0) + 1
                continue
            a, b = spans.get(kind, (lo, hi))
            spans[kind] = (min(a, lo), max(b, hi))
    return {k: f"{a}–{b}" if a != b else str(a) for k, (a, b) in spans.items()}


def volumes(folder):
    unknown = {}
    for page in sorted(pathlib.Path(folder).glob("*.html")):
        for row in re.findall(r"<tr[^>]*>(.*?)</tr>", page.read_text(encoding="utf-8"), re.S):
            m = re.search(r'href="/register/soap-pn/([^"/]+)"[^>]*>([^<]+)</a>', cell(row, "title-field"))
            if not m:
                continue
            portal_id, signature = m.group(1), text(m.group(2))
            names = [place(text(li)) for li in re.findall(r"<li[^>]*>(.*?)</li>", cell(row, "field-doc-place"), re.S)]
            names = [(n, a) for n, a in names if n]
            vol = {"schema": 1, "archive": ARCHIVE, "portal": "portafontium", "portal_id": portal_id,
                   "url": BASE + portal_id, "signature": signature,
                   "parish": re.sub(r"\s+\S*\d\S*$", "", signature) or signature,
                   "places": list(dict.fromkeys(n for n, _ in names)),
                   "aliases": {n: a for n, a in names if a},
                   "records": records(cell(row, "field-doc-dates-field-doc-dates-from-1"), unknown),
                   "points": [], "sources": [{"by": "katalog-portafontium", "date": datetime.date.today().isoformat()}]}
            if not vol["places"]:
                del vol["places"]
            if not vol["aliases"]:
                del vol["aliases"]
            yield vol
    for sign, n in sorted(unknown.items()):
        print(f"neznámá značka druhu „{sign}“: {n}×", file=sys.stderr)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    write = "--zapsat" in argv
    wanted = [a for a in argv[2:] if not a.startswith("--")]
    if not wanted and "--vse" not in argv:
        print(__doc__)
        return 2
    new = skipped = filled = empty = bad = 0
    seen = set()
    for vol in volumes(argv[1]):
        if vol["portal_id"] in seen:
            continue
        seen.add(vol["portal_id"])
        if wanted and not any(vol["portal_id"] == w or (w.endswith("-") and vol["portal_id"].startswith(w))
                              for w in wanted):
            continue
        path = DATA / ARCHIVE / f"{vol['portal_id']}.json"
        if path.exists():
            skipped += 1
            old = json.loads(path.read_text(encoding="utf-8"))
            aliases = {k: v for k, v in (vol.get("aliases") or {}).items() if k in (old.get("places") or [])}
            if aliases and "aliases" not in old:
                filled += 1
                if write:
                    path.write_text(json.dumps({**old, "aliases": aliases}, ensure_ascii=False, indent=1) + "\n",
                                    encoding="utf-8")
            continue
        if not vol["records"]:
            empty += 1
            print(f"bez roků, vynechávám: {vol['portal_id']}", file=sys.stderr)
            continue
        errors = check(path, vol)
        if errors:
            bad += 1
            print(f"{vol['portal_id']}: {errors}", file=sys.stderr)
            continue
        new += 1
        if write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(vol, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"nových svazků: {new}{'' if write else ' (nezapsáno, přidej --zapsat)'}, už v mapě: {skipped} "
          f"(z toho doplněné jiné názvy obcí: {filled}), "
          f"bez roků: {empty}, s chybou: {bad}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
