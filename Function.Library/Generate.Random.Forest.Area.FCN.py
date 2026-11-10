# ============================================================
# Generate.Random.Forest.Area.FCN.py
# ============================================================
# POPIS:
#   Vygeneruje náhodný les na zadaných souřadnicích. V oblasti
#   o zadané šířce a délce rozmístí náhodně stromy (OAK/BIRCH/
#   SPRUCE), keře (vytvořené z listí) a trávu/vysokou trávu
#   na podkladu z trávového bloku (GRASS).
#
# POUŽITÍ:
#   Volá se jednou pro vygenerování celé lesní oblasti na
#   zadaných souřadnicích. Parametry sirka/delka určují
#   rozměr oblasti v osách X/Z.
#
#   Příklad:
#       generate_random_forest_area(0, 60, 0, 20, 20)
#
# PARAMETRY:
#   baseX/baseY/baseZ - souřadnice rohu oblasti (levý spodní
#                        roh, světové souřadnice, baseY je
#                        úroveň podkladu)
#   sirka - šířka oblasti v ose X
#   delka - délka oblasti v ose Z
#
# NÁVRATOVÁ HODNOTA:
#   None
# ============================================================

def generate_random_forest_area(baseX, baseY, baseZ, sirka, delka):
    # Podklad - vrstva trávy po celé oblasti
    blocks.fill(GRASS,
        world(baseX, baseY, baseZ),
        world(baseX + sirka - 1, baseY, baseZ + delka - 1),
        FillOperation.REPLACE)

    stromy = [OAK_LOG, BIRCH_LOG, SPRUCE_LOG]
    listy = [OAK_LEAVES, BIRCH_LEAVES, SPRUCE_LEAVES]

    for i in range(sirka):
        for j in range(delka):
            x = baseX + i
            z = baseZ + j
            nahoda = randint(1, 100)

            if nahoda <= 15:
                # Vygeneruje strom - kmen + koruna
                druh = randint(0, 2)
                vyska_stromu = randint(4, 6)
                blocks.fill(stromy[druh],
                    world(x, baseY + 1, z),
                    world(x, baseY + vyska_stromu, z),
                    FillOperation.REPLACE)
                blocks.fill(listy[druh],
                    world(x - 1, baseY + vyska_stromu, z - 1),
                    world(x + 1, baseY + vyska_stromu + 1, z + 1),
                    FillOperation.REPLACE)
                blocks.place(listy[druh], world(x, baseY + vyska_stromu + 2, z))

            elif nahoda <= 25:
                # Vygeneruje keř - malý shluk listí na zemi
                blocks.place(OAK_LEAVES, world(x, baseY + 1, z))

            elif nahoda <= 60:
                # Vygeneruje trávu nebo vysokou trávu
                if randint(0, 1) == 0:
                    blocks.place(GRASS_PLANT, world(x, baseY + 1, z))
                else:
                    blocks.place(TALL_GRASS, world(x, baseY + 1, z))