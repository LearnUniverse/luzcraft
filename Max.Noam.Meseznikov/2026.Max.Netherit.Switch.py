# ============================================================
# MAX - PŘEPÍNACÍ MECHANISMUS (Minecraft Education Edition)
# ============================================================
# POPIS:
#   Mapa obsahuje dva "spínací" bloky (NETHERITE, DIAMOND)
#   umístěné na konkrétní pozici. Podle toho, který blok je
#   tam umístěn, se buď otevře (odstraní bloky/schodiště) nebo
#   zavře (postaví bloky/žebřík) cesta pro hráče.
#
# HLAVNÍ MECHANIKY:
#   - on_chat("run")    -> spouštěcí event (zatím prázdný)
#   - on_forever()      -> v smyčce kontroluje přítomnost
#                          spínacích bloků a podle nich upravuje
#                          okolní bloky (otevírá/zavírá cestu)
#
# KLÍČOVÉ PRVKY:
#   BLOCK_OF_NETHERITE  - spínač "otevřít cestu" (odstraní bloky)
#   DIAMOND_BLOCK       - spínač "zavřít cestu" (postaví bloky)
#   world(x, y, z)      - konkrétní souřadnice ovlivňovaných bloků
# ============================================================

def on_on_chat():
    pass
player.on_chat("run", on_on_chat)

def on_forever():
    if blocks.test_for_block(BLOCK_OF_NETHERITE, world(-639, 297, 109)):
        player.say("netherite")
        blocks.place(PLANKS_ACACIA, world(-638, 297, 93))
        blocks.place(PLANKS_ACACIA, world(-638, 297, 91))
        blocks.place(PLANKS_ACACIA, world(-636, 297, 89))
        blocks.place(AIR, world(-638, 296, 100))
        blocks.place(AIR, world(-638, 296, 97))
        blocks.place(AIR, world(-638, 297, 94))
        blocks.fill(AIR,
            world(-636, 299, 85),
            world(-636, 298, 85),
            FillOperation.REPLACE)
        blocks.fill(AIR,
            world(-636, 297, 87),
            world(-636, 297, 83),
            FillOperation.REPLACE)
        blocks.place(AIR, world(-636, 289, 82))
        blocks.place(AIR, world(-639, 297, 109))
    if blocks.test_for_block(DIAMOND_BLOCK, world(-637, 297, 109)):
        player.say("diamond")
        blocks.place(PLANKS_DARK_OAK, world(-638, 296, 100))
        blocks.place(PLANKS_DARK_OAK, world(-638, 296, 97))
        blocks.place(PLANKS_DARK_OAK, world(-638, 297, 94))
        blocks.fill(PLANKS_DARK_OAK,
            world(-636, 299, 85),
            world(-636, 298, 85),
            FillOperation.REPLACE)
        blocks.fill(PLANKS_DARK_OAK,
            world(-636, 297, 87),
            world(-636, 297, 83),
            FillOperation.REPLACE)
        blocks.place(LADDER, world(-636, 289, 82))
        blocks.place(AIR, world(-638, 297, 93))
        blocks.place(AIR, world(-638, 297, 91))
        blocks.place(AIR, world(-636, 297, 89))
        blocks.place(AIR, world(-637, 297, 109))
loops.forever(on_forever)
