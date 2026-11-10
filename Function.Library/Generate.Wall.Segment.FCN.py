# ============================================================
# Generate.Wall.Segment.FCN.py
# ============================================================
# POPIS:
#   Vytvoří obvodovou hradební zeď kolem obdélníkového
#   nádvoří na zadaných světových souřadnicích. Zeď má
#   klasický vzhled hradu - plný spodek, ochoz (chodník pro
#   obránce) 1 blok pod cimbuřím a cimbuří (zubatý okraj)
#   nahoře, střídající se plné a prázdné bloky. Nádvoří má
#   také vlastní podlahu. Uprostřed jedné strany je ponechán
#   průchod (brána).
#
# POUŽITÍ:
#   Volá se jednou pro vygenerování celého nádvoří s hradbami.
#   Parametry sirka/delka určují vnitřní rozměr nádvoří,
#   vyska určuje výšku zdi (bez cimbuří).
#
#   Příklad:
#       generate_wall_segment(STONE_BRICKS, 0, 60, 0, 15, 15, 5)
#
# PARAMETRY:
#   material - typ bloku použitý pro zeď (např. STONE_BRICKS)
#   baseX/baseY/baseZ - souřadnice rohu nádvoří (levý spodní
#                        roh, světové souřadnice)
#   sirka - šířka nádvoří v ose X (včetně zdí)
#   delka - délka nádvoří v ose Z (včetně zdí)
#   vyska - výška zdi bez cimbuří
#
# NÁVRATOVÁ HODNOTA:
#   None
# ============================================================

def generate_wall_segment(material, baseX, baseY, baseZ, sirka, delka, vyska):
    maxX = baseX + sirka - 1
    maxZ = baseZ + delka - 1
    topY = baseY + vyska - 1

    # Podlaha nádvoří
    blocks.fill(material,
        world(baseX, baseY - 1, baseZ),
        world(maxX, baseY - 1, maxZ),
        FillOperation.REPLACE)

    # Vyčistí vnitřek nádvoří (prostor pro hráče)
    blocks.fill(AIR,
        world(baseX + 1, baseY, baseZ + 1),
        world(maxX - 1, topY + 2, maxZ - 1),
        FillOperation.REPLACE)

    # Přední stěna (Z = baseZ) - plná zeď
    blocks.fill(material,
        world(baseX, baseY, baseZ),
        world(maxX, topY, baseZ),
        FillOperation.REPLACE)

    # Zadní stěna (Z = maxZ) - plná zeď
    blocks.fill(material,
        world(baseX, baseY, maxZ),
        world(maxX, topY, maxZ),
        FillOperation.REPLACE)

    # Levá stěna (X = baseX) - plná zeď
    blocks.fill(material,
        world(baseX, baseY, baseZ),
        world(baseX, topY, maxZ),
        FillOperation.REPLACE)

    # Pravá stěna (X = maxX) - plná zeď
    blocks.fill(material,
        world(maxX, baseY, baseZ),
        world(maxX, topY, maxZ),
        FillOperation.REPLACE)

    # Brána - průchod široký 2 bloky uprostřed přední stěny
    stredX = baseX + (sirka // 2)
    blocks.fill(AIR,
        world(stredX, baseY, baseZ),
        world(stredX + 1, baseY + 2, baseZ),
        FillOperation.REPLACE)

    # Ochoz - chodník pro obránce 1 blok pod cimbuřím,
    # vystupující dovnitř nádvoří po celém obvodu zdi
    blocks.fill(material,
        world(baseX + 1, topY, baseZ + 1),
        world(maxX - 1, topY, baseZ + 1),
        FillOperation.REPLACE)

    blocks.fill(material,
        world(baseX + 1, topY, maxZ - 1),
        world(maxX - 1, topY, maxZ - 1),
        FillOperation.REPLACE)

    blocks.fill(material,
        world(baseX + 1, topY, baseZ + 1),
        world(baseX + 1, topY, maxZ - 1),
        FillOperation.REPLACE)

    blocks.fill(material,
        world(maxX - 1, topY, baseZ + 1),
        world(maxX - 1, topY, maxZ - 1),
        FillOperation.REPLACE)

    # Cimbuří po celém obvodu - střídavé bloky nad vrcholem zdi
    for i in range(sirka):
        if i % 2 == 0:
            blocks.place(material, world(baseX + i, topY + 1, baseZ))
            blocks.place(material, world(baseX + i, topY + 1, maxZ))

    for i in range(delka):
        if i % 2 == 0:
            blocks.place(material, world(baseX, topY + 1, baseZ + i))
            blocks.place(material, world(maxX, topY + 1, baseZ + i))