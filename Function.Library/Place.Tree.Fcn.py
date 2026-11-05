
# Funkce zasadStrom(naX, naY, naZ, strom)
#   Zasadí strom na zadaných souřadnicích.
#   Parametry:
#     naX, naY, naZ - souřadnice, kam se strom zasadí
#     strom         - název stromu (feature) z Minecraftu, např. "oak_tree_feature" (seznam níže)
#   Postup:
#     1) složí příkaz "/place feature minecraft:<strom> X Y Z" a uloží ho do prikazStrom
#     2) pod místo výsadby (Y - 1) položí blok trávy, aby strom měl na čem růst
#     3) příkaz provede přes player.execute
#
# Názvy stromů pro Bedrock / Education (zdroj: minecraft.wiki/w/Tree):
#   Dub:        oak_tree_feature, fancy_oak_tree_feature, swamp_tree_feature,
#               oak_tree_with_vines_feature, fancy_oak_tree_with_leaf_litter_and_optional_beehive
#   Bříza:      birch_tree_feature, super_birch_tree_feature
#   Smrk:       spruce_tree_feature, pine_tree_feature, mega_spruce_tree_feature,
#               mega_pine_tree_feature, mountain_spruce_tree_feature, mountain_pine_tree_feature,
#               spruce_tree_with_vines_feature
#   Džungle:    jungle_tree_feature, mega_jungle_tree_feature, jungle_bush_feature,
#               undecorated_jungle_tree_feature, undecorated_jungle_tree_with_vines_feature
#   Akácie:     savanna_tree_feature
#   Tmavý dub:  roofed_tree_feature, roofed_tree_with_vines_feature
#   Mangrovy:   mangrove_tree_feature, tall_mangrove_tree_feature,
#               mangrove_tree_with_beenest_feature, tall_mangrove_tree_with_beenest_feature
#   Azalka:     azalea_tree_feature
#   Třešeň:     cherry_tree_feature, cherry_tree_with_beehive_feature
#   Bledý dub:  pale_oak_tree_feature, pale_oak_tree_with_decorations_feature,
#               pale_oak_tree_with_decorations_and_creaking_heart_feature
#   Topol:      red_poplar_tree_feature, orange_poplar_tree_feature, yellow_poplar_tree_feature
#   Padlé:      fallen_oak_tree_feature, fallen_birch_tree_feature, fallen_super_birch_tree_feature,
#               fallen_spruce_tree_feature, fallen_jungle_tree_feature, fallen_poplar_tree_feature
#   (některé nejnovější typy, např. topoly, nemusí být ve starších verzích Education)

prikazStrom = ""
pX = 0
pY = 0
pZ = 0

def zasadStrom(naX: number, naY: number, naZ: number, strom: str):
    global prikazStrom
    prikazStrom = "/place feature minecraft:" + strom + " " + ("" + str(naX)) + " " + ("" + str(naY)) + " " + ("" + str(naZ))
    blocks.place(GRASS, world(naX, naY - 1, naZ))
    player.execute(prikazStrom)

def on_on_chat():
    global pX, pY, pZ
    pX = player.position().get_value(Axis.X)
    pY = player.position().get_value(Axis.Y)
    pZ = player.position().get_value(Axis.Z)
    for index in range(4):
        zasadStrom(pX, pY, pZ, "cherry_tree_feature ")
        pZ += randint(2, 6)
player.on_chat("strom", on_on_chat)
