<!-- filepath: /Users/pavelvondruska/Downloads/REPO/luzcraft/.github/copilot-instructions.md -->
# Instrukce pro generování kódu - Minecraft Education Edition

## Obecná pravidla
- Veškerý kód se píše v jazyce **Python**.
- Kód je určen pro **Minecraft Education Edition** (používá se API `blocks`, `player`, `mobs`, `world`, `Axis`, `FillOperation`, atd.).
- Před každým funkčním blokem (funkcí, souborem) musí být **hlavičkový komentář**, který stručně a jasně popisuje:
  - co daná funkce/soubor dělá,
  - jaké je očekávané použití (vstupy, výstupy, kontext volání).

## Umístění nových funkcí
- Pokud je požadována **nová samostatná funkce** (knihovní, znovupoužitelná), vždy se ukládá do adresáře:
## Pojmenování souborů a funkcí
- Název souboru/funkce se píše **camel** způsobem, kde jednotlivá slova jsou oddělena **tečkou** (ne podtržítkem, ne CamelCase bez teček).
- Příklad: `Generate.Random.Platform.FCN.py`
- Název musí být **zkratkovým popisem funkčnosti** - stručně vystihuje, co funkce dělá (ne obecné názvy jako `Helper` nebo `Utils`).
- Na **konec názvu** se vždy přidává zkratka `FCN` (Function), oddělená tečkou.
- Formát: `Slovo1.Slovo2.Slovo3.FCN.py`

## Struktura hlavičky souboru/funkce
Každý soubor ve `Function.Library` musí obsahovat hlavičku v tomto formátu:

```python
# ============================================================
# NÁZEV FUNKCE (popisný, lidsky čitelný)
# ============================================================
# POPIS:
#   Stručný popis toho, co funkce dělá.
#
# POUŽITÍ:
#   Jak a kdy funkci volat, jaké jsou parametry a návratová
#   hodnota (pokud existuje).
#
# PARAMETRY:
#   nazev_parametru - popis parametru
#
# NÁVRATOVÁ HODNOTA:
#   popis návratové hodnoty (pokud existuje)
# ============================================================# ============================================================
# Generate.Random.Platform.FCN.py
# ============================================================
# POPIS:
#   Vygeneruje náhodnou platformu z daného bloku na zadaných
#   souřadnicích s náhodným posunem v ose X a Z.
#
# POUŽITÍ:
#   Volá se opakovaně ve smyčce pro generování parkurových
#   platforem nebo jiných herních struktur.
#
# PARAMETRY:
#   blockType - typ bloku (např. WHITE_CONCRETE)
#   baseX/baseY/baseZ - výchozí souřadnice generování
#
# NÁVRATOVÁ HODNOTA:
#   None
# ============================================================

def generate_random_platform(blockType, baseX, baseY, baseZ):
    x = baseX + randint(-5, 5)
    z = baseZ + randint(-5, 5)
    blocks.place(blockType, world(x, baseY, z))