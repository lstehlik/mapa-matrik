import json, os, sys

OUT = sys.argv[1]
SRC = [{"by": "ondrnovy", "date": "2026-11-10"}]
E = "https://ebadatelna.soapraha.cz"
P = "https://www.portafontium.eu/register/soap-pn/"

def eb(pid, sig, parish, records, scans, places, order, points, index=None, sections=None, notes=None, lang=None, district="Rakovník"):
    return dict(schema=1, archive="soa-praha", portal="ebadatelna", portal_id=str(pid),
                url=f"{E}/pages/MatrikaPage/matrikaId/{pid}", scan_url=f"{E}/d/{pid}/{{scan}}",
                signature=sig, parish=parish, district=district, places=places, records=records, scans=scans,
                language=lang, order=order, index=index, points=points, sections=sections or [], notes=notes or [], sources=SRC)

def pf(slug, sig, parish, records, scans, places, order, points, index=None, sections=None, notes=None, lang=None, district=None):
    return dict(schema=1, archive="soa-plzen", portal="portafontium", portal_id=slug, url=P + slug,
                scan_url=None, signature=sig, parish=parish, district=district, places=places, records=records,
                scans=scans, language=lang, order=order, index=index, points=points, sections=sections or [],
                notes=notes or [], sources=SRC)

V = []

V.append(eb(4887, "Čistá 04", "Čistá", {"N": "1687–1731", "O": "1688–1731", "Z": "1688–1731"}, 281,
    ["Čistá", "Krakov", "Břežany", "Zavidov", "Zdeslav", "Šípy", "Kůzová", "Křekovice", "Všesulov"], "chronological",
    [dict(scan=45, type="N", year=1698, year_to=1699), dict(scan=51, type="N", year=1700, months="VIII–XII"),
     dict(scan=52, type="N", year=1701, months="I–III", note="nadpis „Letha 1701“"),
     dict(scan=55, type="N", year=1702, months="I–III", note="nadpis „Letha 1702“"),
     dict(scan=57, type="N", year=1702, months="VII–IX"), dict(scan=58, type="N", year=1702, year_to=1703, months="X–I")],
    notes=["Bez rejstříku. Zápisy česky, u každého ves na začátku řádku („z Kratowa“ = Krakov)."], lang="čeština"))

V.append(eb(4888, "Čistá 05", "Čistá", {"N": "1731–1777", "O": "1732–1777", "Z": "1732–1777"}, 395,
    ["Čistá", "Krakov", "Břežany", "Křekovice", "Kůzová", "Šípy", "Všesulov", "Zavidov", "Zdeslav"], "chronological",
    [dict(scan=20, type="N", year=1735, page="30–31"), dict(scan=22, type="N", year=1736, months="I–III", page="34–35"),
     dict(scan=81, type="N", year=1748, page="150–151"), dict(scan=82, type="N", year=1749, page="152–153"),
     dict(scan=208, type="O", year=1732, year_to=1733, page="2–3"), dict(scan=212, type="O", year=1734, year_to=1735, page="10–11"),
     dict(scan=250, type="O", year=1758, year_to=1759, page="86–87"), dict(scan=265, type="O", year=1771, page="116–117"),
     dict(scan=307, type="Z", year=1744, page="70–71"), dict(scan=375, type="Z", year=1772, months="I", page="206–207")],
    index={"volume": "soa-praha/5863 (N 1732–1760, Z 1732–1777), soa-praha/5864 (N 1761–1790), soa-praha/5866 (O 1732–1777)", "refers_to": "page"},
    sections=[dict(scans="1–~205", type="N", years="1731–1777"), dict(scans="~206–~300", type="O", years="1732–1777"),
              dict(scans="~300–395", type="Z", years="1732–1777")],
    notes=["Hranice oddílů N/O/Z odhadnuté z bodů, ne přesně ověřené.", "Latina, u sňatků 1732–1733 česky.",
           "I 1772: neobvykle mnoho úmrtí (hladomor 1771–1772)."], lang="latina"))

V.append(eb(4889, "Čistá 06", "Čistá", {"N": "1778–1817", "Z": "1778–1799"}, 200,
    ["Čistá", "Krakov", "Bělbožice", "Břežany", "Křekovice", "Kůzová", "Nová Ves", "Šípy", "Strachovice", "Všesulov", "Zavidov", "Zdeslav"], "chronological",
    [dict(scan=2, type="title"), dict(scan=6, type="N", year=1778, year_to=1779, months="X–III", page="4–5"),
     dict(scan=7, type="N", year=1779, page="6–7"), dict(scan=10, type="N", year=1780, months="XI"),
     dict(scan=13, type="N", year=1781), dict(scan=14, type="N", year=1781, months="XI", page="20–21"),
     dict(scan=19, type="N", year=1783, months="I", page="30–31"), dict(scan=23, type="N", year=1783, page="38–39"),
     dict(scan=24, type="N", year=1784, months="I–IV"), dict(scan=25, type="N", year=1784, page="42–43"),
     dict(scan=26, type="N", year=1786, months="I–II", page="44–45"), dict(scan=27, type="N", year=1786),
     dict(scan=28, type="N", year=1786, months="VII–X"), dict(scan=29, type="N", year=1786, months="X–XII"),
     dict(scan=30, type="N", year=1786, year_to=1787, months="XII–I"), dict(scan=31, type="N", year=1787, months="I–II", page="54–55"),
     dict(scan=32, type="N", year=1787, note="vpravo květen"), dict(scan=33, type="N", year=1787, months="V", page="58–59"),
     dict(scan=34, type="N", year=1787, months="VI–VIII"), dict(scan=35, type="N", year=1787, months="IX–XI"),
     dict(scan=36, type="N", year=1787, year_to=1788, months="XI–I"), dict(scan=37, type="N", year=1788, months="I–IV"),
     dict(scan=38, type="N", year=1788, months="IV–VII"), dict(scan=39, type="N", year=1788, months="VII–VIII"),
     dict(scan=40, type="N", year=1788, months="IX–XI"),
     dict(scan=41, type="N", year=1789, months="I–II"), dict(scan=42, type="N", year=1789, months="III–IV"),
     dict(scan=43, type="N", year=1789, months="V–VII"), dict(scan=44, type="N", year=1789, months="VIII–XII"),
     dict(scan=45, type="N", year=1790, months="I–II"), dict(scan=46, type="N", year=1790, months="II–VII"),
     dict(scan=47, type="N", year=1790, months="VII–IX"), dict(scan=48, type="N", year=1790, months="X–XII"),
     dict(scan=49, type="N", year=1791, months="I–V"), dict(scan=50, type="N", year=1791, months="V–VII"),
     dict(scan=51, type="N", year=1791, months="VIII–XII"), dict(scan=52, type="N", year=1792, months="I–III"),
     dict(scan=53, type="N", year=1792, months="III–VIII"), dict(scan=65, type="N", year=1795, months="XI–XII")],
    index={"volume": "soa-praha/5864 (N 1761–1790)", "refers_to": "page", "note": "stránkování rejstříku u let 1784–1787 nesedí"},
    notes=["Rok 1785 chybí – je v knize Čistá 07 (soa-praha/4890).",
           "Sn. 51 dole vlevo: dodatečný zápis křtu (z r. 1824), část zakrytá proužkem papíru."], lang="latina"))

V.append(eb(4890, "Čistá 07", "Čistá", {"N": "1784–1785", "O": "1784–1785", "Z": "1784–1785"}, 52,
    ["Čistá", "Krakov", "Břežany", "Křekovice", "Šípy", "Všesulov", "Zavidov", "Zdeslav"], "by_village",
    [dict(scan=4, type="N", year=1784, page="4–5"), dict(scan=12, type="Z", year=1784, year_to=1785, page="2–3"),
     dict(scan=23, type="O", note="prázdné stránky, přelepený list"),
     dict(scan=24, type="N", year=1784, year_to=1785, months="V–III", page="57", place="Krakov")],
    notes=["Tištěné německé formuláře (Geburtsbuch / Trauungsbuch / Sterbregister) z josefínské reformy 1784."], lang="latina"))

V.append(eb(5858, "Čistá 16", "Čistá", {"O": "1778–1824", "iO": "1778–1824"}, 63,
    ["Čistá", "Krakov", "Břežany", "Křekovice", "Kůzová", "Milíčov", "Šípy", "Václavy", "Všesulov", "Zavidov", "Zdeslav"], "chronological",
    [dict(scan=3, type="O", year=1778, months="I–IX", page="1"), dict(scan=4, type="O", year=1778, year_to=1779, months="XI–XI", page="2–3"),
     dict(scan=56, type="O", year=1820, year_to=1821, page="106–107"), dict(scan=60, type="iO", letters="A–F"),
     dict(scan=61, type="iO", letters="G–Ž (?)")],
    index={"scans": "60–61", "by": "groom", "refers_to": "folio"},
    notes=["Rejstřík poškozený, část písmene R nečitelná."], lang="latina"))

V.append(eb(5859, "Čistá 17", "Čistá", {"O": "1805–1850", "iO": "1805–1850"}, 137,
    ["Čistá", "Krakov", "Břežany", "Křekovice", "Kůzová", "Šípy", "Všesulov"], "by_village",
    [dict(scan=105, type="O", year=1824, page="212", place="Krakov"), dict(scan=108, type="O", year=1834, year_to=1847, page="218–219", place="Krakov"),
     dict(scan=128, type="iO", letters="L")],
    index={"scans": "125–128", "refers_to": "page"},
    notes=["Mikrofilm, nízký kontrast."], lang="latina"))

V.append(eb(5863, "Čistá 21", "Čistá", {"iN": "1732–1760", "iZ": "1732–1778"}, 49, ["Čistá", "Krakov"], "mixed",
    [dict(scan=10, type="iN", letters="L"), dict(scan=14, type="iN", note="jiné písmeno"), dict(scan=34, type="iZ", letters="L"), dict(scan=36, type="iZ")],
    index={"refers_to": "page", "volume": "soa-praha/4888"}, notes=["Rejstřík ke knize Čistá 05; uvádí rok a stranu."]))

V.append(eb(5864, "Čistá 22", "Čistá", {"iN": "1761–1790"}, 23, ["Čistá", "Krakov"], "mixed",
    [dict(scan=10, type="iN", letters="K (?)"), dict(scan=11, type="iN", letters="L")],
    index={"refers_to": "page", "volume": "soa-praha/4888, soa-praha/4889"},
    notes=["U let 1783–1787 strany v rejstříku nesedí se stranami knihy Čistá 06; jedna dcera zapsaná pod jménem otce."]))

V.append(eb(5866, "Čistá 24", "Čistá", {"iO": "1732–1777"}, 15, ["Čistá", "Krakov"], "mixed",
    [dict(scan=1, type="iO"), dict(scan=7, type="iO", letters="L–M")],
    index={"refers_to": "page", "volume": "soa-praha/4888"}, notes=["Ženichové i nevěsty podle příjmení, rok a strana knihy Čistá 05."]))

V.append(eb(5871, "Čistá 29", "Čistá", {"O": "1849–1942"}, 245,
    ["Bělbožice", "Břežany", "Krakov", "Křekovice", "Kůzová", "Šípy", "Václavský Nový Dvůr", "Všesulov"], "by_village_bride",
    [dict(scan=35, type="O", year=1886, year_to=1887, page="33", place="Břežany"),
     dict(scan=60, type="O", year=1857, year_to=1858, page="58", place="Šostov (?)"),
     dict(scan=80, type="O", year=1890, year_to=1891, page="78", place="Všesulov"),
     dict(scan=105, type="O", year=1860, year_to=1863, page="103", place="Krakov"),
     dict(scan=109, type="O", year=1864, page="107", place="Krakov"),
     dict(scan=111, type="O", year=1870, year_to=1872, page="109", place="Bělbožice"),
     dict(scan=117, type="O", year=1881, year_to=1884, page="115", place="Bělbožice"),
     dict(scan=125, type="O", year=1919, year_to=1920, page="123", place="Bělbožice"),
     dict(scan=130, type="O", year=1850, year_to=1851, place="Šípy"),
     dict(scan=170, type="O", year=1938, year_to=1941, place="Šípy", note="konec oddílu"),
     dict(scan=172, type="blank"),
     dict(scan=190, type="O", year=1905, year_to=1906, place="Křekovice"),
     dict(scan=240, type="O", year=1930, year_to=1933, place="Kůzová")],
    sections=[dict(scans="~100–110", type="O", place="Krakov", years="1849–1864 (pokračování po 1864 nenalezeno)"),
              dict(scans="111–~128", type="O", place="Bělbožice", years="1870–1920"),
              dict(scans="130–170", type="O", place="Šípy", years="1850–1941"),
              dict(scans="173–~200", type="O", place="Křekovice"),
              dict(scans="~230–245", type="O", place="Kůzová", years="–1933")],
    notes=["Bez rejstříku. Zápis je v oddílu vsi NEVĚSTY (ženich z Krakova může být u Bělbožic).",
           "Strana knihy = snímek − 2 (ověřeno u sn. 35–125)."], lang="čeština"))

V.append(eb(11250, "Petrovice-RA 09", "Petrovice", {"N": "1827–1865", "iN": "1827–1865"}, 379,
    ["Petrovice", "Příčina", "Řeřichy", "Žďár"], "by_village",
    [dict(scan=2, type="title"), dict(scan=171, type="N", year=1832, page="fol. 176", place="Příčina"),
     dict(scan=172, type="N", year=1832, months="VIII", page="fol. 177", place="Příčina"),
     dict(scan=196, type="N", year=1842, place="Příčina"), dict(scan=200, type="N", year=1844, place="Příčina"),
     dict(scan=250, type="N", year=1860, place="Příčina"), dict(scan=255, type="N", place="Příčina"),
     dict(scan=256, type="N", year=1863, place="Příčina"), dict(scan=330, type="N", place="Řeřichy")],
    notes=["Příčina od ~fol. 200 / ~sn. 165 do 1864."], lang="latina / čeština"))

V.append(eb(11265, "Petrovice-RA 20", "Petrovice", {"N": "1858–1874", "O": "1859–1874", "Z": "1859–1875"}, None,
    ["Příčina", "Žďár"], "mixed",
    [dict(scan=66, type="N", year=1874, months="VI", page="63"), dict(scan=68, type="O", year=1859, year_to=1862, page="65", note="všechny sňatky 1859–1862"),
     dict(scan=69, type="O", year=1863, year_to=1865, page="66"), dict(scan=71, type="O", year=1868, page="68"),
     dict(scan=88, type="Z", year=1868, page="100"),
     dict(scan=106, type="iN", letters="F"), dict(scan=108, type="iN", letters="H"), dict(scan=109, type="iN", letters="J"),
     dict(scan=110, type="iN"), dict(scan=111, type="iN", letters="L")],
    index={"scans": "101–111", "note": "společný rejstřík N/O/Z, sloupce podle druhu"},
    notes=["Rejstřík u jednoho zápisu z r. 1868 uvádí jiné křestní jméno než zápis v knize."], lang="čeština"))

V.append(eb(11266, "Petrovice-RA 21", "Petrovice", {"N": "1874–1892", "O": "1874–1899", "Z": "1876–1915"}, 232,
    ["Příčina", "Žďár"], "mixed",
    [dict(scan=120, type="O", year=1886, page="118"), dict(scan=136, type="O", year=1897, page="134"),
     dict(scan=196, type="Z", year=1902, year_to=1903, page="199"), dict(scan=198, type="Z", year=1905, page="201"),
     dict(scan=205, type="Z", year=1909, page="208"), dict(scan=207, type="Z", year=1910, year_to=1911, page="210"),
     dict(scan=208, type="Z", year=1911, year_to=1912, page="211"),
     dict(scan=219, type="iN", letters="J"), dict(scan=220, type="iN", letters="L"), dict(scan=229, type="iN", letters="V")],
    index={"scans": "~215–232", "note": "společný rejstřík N/O/Z"},
    notes=["Rejstřík Z 12. 11. 1902 „Jaroš“ je ve skutečnosti Janoušek."], lang="čeština"))

V.append(eb(8224, "Lužná 02", "Lužná", {"N": "1830–1870", "iN": "1830–1870"}, 272, ["Lužná", "Belšanka"], "chronological",
    [dict(scan=208, type="N", year=1866, page="fol. 206"), dict(scan=250, type="iN", letters="E–F"), dict(scan=253, type="iN", letters="H")],
    index={"scans": "250–~260", "refers_to": "folio"}, lang="čeština"))

V.append(eb(8229, "Lužná 07", "Lužná", {"O": "1847–1889", "Z": "1847–1878"}, 144, ["Lužná"], "mixed",
    [dict(scan=134, type="iO", letters="K"), dict(scan=135, type="iO", letters="L–M")],
    index={"scans": "~128–144", "refers_to": "folio"}, lang="čeština"))

V.append(pf("chric-12", "Chříč 12", "Chříč", {"N": "1848–1891"}, 99, ["Slatina", "Březsko"], "chronological",
    [dict(scan=60, type="N", year=1878), dict(scan=74, type="N", year=1880, months="VII–XII", page="73"),
     dict(scan=76, type="N", year=1881, months="III–VII", page="75")],
    index={"volume": "soa-plzen/chric-14", "refers_to": "page"}, notes=["Dvůr Březsko zapisován do knihy Slatiny."], lang="čeština", district="Plzeň-sever"))

V.append(pf("chric-14", "Chříč 14", "Chříč", {"iN": "1786–1910", "iO": "1786–1910", "iZ": "1786–1910"}, 105,
    ["Chříč", "Hlince", "Holovousy", "Lhota", "Slatina", "Studená"], "mixed",
    [dict(scan=64, type="iN", letters="P", year=1864, year_to=1881), dict(scan=70, type="iN", letters="R", year=1880, year_to=1908)],
    notes=["Jeden rejstřík pro všechny knihy fary 1786–1910, uvnitř písmene po letech; sloupce narozených / oddaných / zemřelých."], district="Plzeň-sever"))

V.append(pf("kozlany-21", "Kožlany 21", "Kožlany", {"O": "1895–1949", "iO": "1895–1949"}, 189, ["Kožlany"], "chronological",
    [dict(scan=45, type="O", year=1903, page="43"), dict(scan=60, type="O", year=1906, page="58"),
     dict(scan=117, type="O", year=1926, note="přibližně"), dict(scan=120, type="O", year=1929), dict(scan=139, type="O", year=1941),
     dict(scan=147, type="O", year=1945), dict(scan=175, type="iO", letters="M"), dict(scan=176, type="iO", letters="N")],
    index={"scans": "~160–189", "refers_to": "page", "note": "po ~1923 neúplný"}, district="Plzeň-sever"))

V.append(pf("kozlany-22", "Kožlany 22", "Kožlany", {"Z": "1900–1949", "iZ": "1900–1949"}, 144, ["Kožlany"], "chronological",
    [dict(scan=38, type="Z", page="fol. 36"), dict(scan=62, type="Z", year=1914, page="fol. 60"), dict(scan=74, type="Z", year=1918, page="fol. 72"),
     dict(scan=136, type="iZ", letters="M–N")],
    index={"scans": "~125–144", "refers_to": "folio", "note": "po ~1930 neúplný"}, district="Plzeň-sever"))

V.append(pf("kozlany-14", "Kožlany 14", "Kožlany", {"N": "1862–1879", "iN": "1862–1879"}, 221, ["Kožlany"], "chronological",
    [dict(scan=157, type="N", year=1876, page="154"), dict(scan=212, type="iN", letters="N")], index={"scans": "~200–221", "refers_to": "page"}, district="Plzeň-sever"))

V.append(pf("kozlany-17", "Kožlany 17", "Kožlany", {"O": "1838–1895"}, 286, ["Kožlany"], "chronological",
    [dict(scan=16, type="O", year=1844, page="13"), dict(scan=17, type="O", year=1844, page="14"),
     dict(scan=74, type="O", year=1863, page="fol. 70"), dict(scan=82, type="O", year=1866, page="fol. 78", note="přibližně")], district="Plzeň-sever"))

V.append(pf("kozlany-09", "Kožlany 09", "Kožlany", {"N": "1829–1850"}, 164, ["Kožlany"], "chronological",
    [dict(scan=69, type="N", year=1839), dict(scan=70, type="N", year=1839, months="IX", page="134"),
     dict(scan=71, type="N", year=1839)], district="Plzeň-sever"))

V.append(pf("kozojedy-11", "Kozojedy 11", "Kozojedy", {"N": "1856–1880"}, 62, ["Bohy"], "chronological",
    [dict(scan=58, type="N", year=1879), dict(scan=61, type="N", year=1880, months="I–V")], district="Plzeň-sever"))

V.append(pf("kozojedy-17", "Kozojedy 17", "Kozojedy", {"O": "1856–1945"}, 51, ["Bohy"], "chronological",
    [dict(scan=10, type="O", year=1862, note="přibližně"), dict(scan=16, type="O", year=1865, page="13"), dict(scan=22, type="O", year=1880, note="přibližně")], district="Plzeň-sever"))

V.append(pf("liblin-01", "Liblín 01", "Liblín", {"N": "1822–1843"}, 309, ["Bujesily"], "by_village",
    [dict(scan=143, type="N", year=1828, place="Bujesily", note="přibližně"), dict(scan=156, type="N", year=1836, page="324", place="Bujesily"),
     dict(scan=158, type="N", year=1838, place="Bujesily", note="přibližně")],
    sections=[dict(scans="~130–185", type="N", place="Bujesily", years="1822–1843", note="str. 264–375")], district="Rokycany"))

V.append(pf("kralovice-okresni-urad-10", "Kralovice – okresní úřad 10", "Kralovice (civilní)", {"O": "1931–1947"}, 302,
    ["Kralovice", "Kožlany", "Bohy", "Břežany", "okres Kralovice (výběr)"], "chronological",
    [dict(scan=101, type="O", year=1935, months="II", note="přibližně"), dict(scan=105, type="O", year=1935), dict(scan=197, type="O", year=1940, months="IV"),
     dict(scan=260, type="O", year=1944, note="přibližně")], notes=["Civilní sňatky (bez vyznání); 2 zápisy na snímek; 1942–1944 německy."], district="Plzeň-sever"))

for v in V:
    v = {k: val for k, val in v.items() if val is not None}
    v["points"] = [{k: val for k, val in p.items() if val is not None} for p in v["points"]]
    d = os.path.join(OUT, v["archive"]); os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, v["portal_id"] + ".json"), "w", encoding="utf-8") as f:
        json.dump(v, f, ensure_ascii=False, indent=1); f.write("\n")
print(len(V), "svazků")
