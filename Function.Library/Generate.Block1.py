# ============================================================
# Build.Corner.Tower.Platform.FCN.py
# ============================================================
# POPIS:
#   Vytvoří malou stavbu "Rohová plošina" - základovou desku
#   5x5, čtyři rohové sloupy (výška 2 bloky), mezipatro/strop
#   5x5 a čtyři samostatné rohové věžičky na vrcholu.
#
# POUŽITÍ:
#   Volá se jednou pro vygenerování stavby na zadaných
#   souřadnicích. Lze spustit i chatovým příkazem "stavba",
#   který postaví strukturu z GRASS bloku na pozici (0,0,0).
#
#   Příklad:
#       build_corner_tower_platform(GRASS, 0, 0, 0)
#
# PARAMETRY:
#   material - typ bloku použitý pro celou stavbu (např. GRASS)
#   baseX/baseY/baseZ - souřadnice levého předního rohu
#                        základové desky (světové souřadnice)
#
# NÁVRATOVÁ HODNOTA:
#   None
# ============================================================

def build_corner_tower_platform(material, baseX, baseY, baseZ):
    # 1. Vrstva (y = 0): Základová deska 5x5
    blocks.fill(material,
        world(baseX, baseY, baseZ),
        world(baseX + 4, baseY, baseZ + 4),
        FillOperation.REPLACE)

    # 2. a 3. Vrstva (y = 1 až y = 2): 4 rohové sloupy
    # Přední levý roh
    blocks.fill(material,
        world(baseX, baseY + 1, baseZ),
        world(baseX, baseY + 2, baseZ),
        FillOperation.REPLACE)
    # Přední pravý roh
    blocks.fill(material,
        world(baseX + 4, baseY + 1, baseZ),
        world(baseX + 4, baseY + 2, baseZ),
        FillOperation.REPLACE)
    # Zadní levý roh
    blocks.fill(material,
        world(baseX, baseY + 1, baseZ + 4),
        world(baseX, baseY + 2, baseZ + 4),
        FillOperation.REPLACE)
    # Zadní pravý roh
    blocks.fill(material,
        world(baseX + 4, baseY + 1, baseZ + 4),
        world(baseX + 4, baseY + 2, baseZ + 4),
        FillOperation.REPLACE)

    # 4. Vrstva (y = 3): Mezipatro / Strop 5x5
    blocks.fill(material,
        world(baseX, baseY + 3, baseZ),
        world(baseX + 4, baseY + 3, baseZ + 4),
        FillOperation.REPLACE)
    # 4b. Vrstva (y = 3): Mezipatro / Stropni dira 4x4
    blocks.fill(AIR,
        world(baseX + 1, baseY + 3, baseZ + 1),
        world(baseX + 3, baseY + 3, baseZ + 3),
        FillOperation.REPLACE)

    # 5. Vrstva (y = 4): Rohové věžičky (4 samostatné bloky v rozích)
    blocks.place(material, world(baseX, baseY + 4, baseZ))
    blocks.place(material, world(baseX + 4, baseY + 4, baseZ))
    blocks.place(material, world(baseX, baseY + 4, baseZ + 4))
    blocks.place(material, world(baseX + 4, baseY + 4, baseZ + 4))


def on_on_chat():
    build_corner_tower_platform(GRASS, 0, 0, 0)

# Spuštění příkazem "stavba" v chatu
mx = 0
My = 0
mz = 0
# Spuštění příkazem "stavba" v chatu

def on_on_chat():
    global mx, My, mz
    mx = player.position().get_value(Axis.X)
    My = player.position().get_value(Axis.Y)
    mz = player.position().get_value(Axis.Z)
    obracena_stolicka(CYAN_WOOL, mx, My, mz + 5)
player.on_chat("stavba", on_on_chat)