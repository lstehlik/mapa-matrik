# Přispívání

Mapu plní hlavně AI agenti při práci s matrikami; lidé jsou vítaní stejně.

## Co zapisovat

- **Jen to, co je na snímku vidět**: rok, měsíce, strana, ves, druh zápisu, začátek rejstříku, titulní list.
  Žádné odhady – ty počítá až vyhledávání.
- **Žádná jména osob**, žádné přepisy, žádné snímky. Poznámky krátce (do 300 znaků) a věcně
  („rok 1785 chybí“, „strany přečíslované od 120“).
- Nesouhlasí-li existující bod s tím, co vidíš, **přidej vlastní bod**, neopravuj cizí. Vyhledávání ukáže oba.

## Jak se příspěvek dostane do mapy

1. `pridej_bod` / `pridej_svazek` (MCP) uloží bod lokálně.
2. `python3 tools/body.py odeslat <klon>` vytvoří větev, doplní `by` = tvůj účet GitHubu a pošle pull request.
3. Akce `kontrola PR` (kód z `main`, z PR čte jen data):
   - **chyba formátu** (neznámé pole, snímek mimo rozsah knihy, špatný druh) → PR neprojde, oprav a pošli znovu;
   - **jen přidání** bodů nebo nových knih, body s `by` = autor PR, nejvýš 200 bodů → **sloučí se automaticky**
     a mapa na webu se do pár minut obnoví;
   - **cokoli jiného** (změna nebo smazání existujících dat, soubory mimo `data/`, možné jméno nebo kontakt
     v poznámce) → štítek `ke-kontrole`, rozhodne správce.

## Ověřené body

Bod, který nezávisle zapíší dva různí přispěvatelé, je ve zveřejněných datech `verified: true`.
Stejný bod od druhého účtu tedy není zbytečný – potvrzuje ho.

## Správce

Sloučení PR se štítkem `ke-kontrole` a změny kódu (`tools/`, `.github/`) jsou jen na správci.
Každou změnu lze vrátit (`git revert`).
