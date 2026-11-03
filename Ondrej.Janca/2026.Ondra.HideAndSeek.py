# ============================================================
# MULTI ARENA - Minecraft Education Edition
# ============================================================
# POPIS:
#   Sada minihry s více aktivitami spouštěnými chatovými
#   příkazy: parkur přes náhodné bloky nad lávou, bludiště
#   s villagery a efekty, droper (pád přes pavučiny) a výdej
#   diamantového meče s oslepením nejbližšího hráče.
#
# HLAVNÍ MECHANIKY:
#   - on_chat("podlaha") -> zaplaví arénu lávou (past pod parkurem)
#   - on_chat("bludiste")-> vygeneruje 40 náhodných bílých
#                          betonových stěn, osleptí/posílí
#                          všechny entity a vyspawnuje villagery
#   - on_chat("run")     -> dá náhodnému hráči diamantový meč
#                          a oslepí nejbližšího hráče
#   - on_chat("parkur")  -> vygeneruje 20 párů náhodných
#                          platforem (WHITE_CONCRETE) nad lávou
#   - on_chat("Droper")  -> vygeneruje 40 cobwebů (pavučin) na
#                          náhodných pozicích pro pád hráče
#
# KLÍČOVÉ PROMĚNNÉ:
#   X2/Y/Z2              - náhodné souřadnice pro generování
#                          bloků/moba v jednotlivých minihrách
# ============================================================



def jedna_cast_parkuru():
    global X2, Z2
    X2 = randint(-10, -17)
    Z2 = randint(-9, -34)
    blocks.place(WHITE_CONCRETE, world(X2, -58, Z2))
    X2 = randint(-10, -17)
    Z2 = randint(-9, -34)
    blocks.place(WHITE_CONCRETE, world(X2, -58, Z2))
    player.say(":)")

def on_on_chat():
    blocks.fill(LAVA,
        world(-10, -59, -9),
        world(-17, -60, -34),
        FillOperation.REPLACE)
player.on_chat("podlaha", on_on_chat)

def JEDNASTĚNABLUDIŠTĚ():
    global Z2, X2
    Z2 = randint(5, 35)
    X2 = randint(-9, -15)
    blocks.place(WHITE_CONCRETE, world(X2, -59, Z2))
    blocks.place(WHITE_CONCRETE, world(X2, -58, Z2))
    player.say(":)")

def on_on_chat2():
    for index in range(40):
        JEDNASTĚNABLUDIŠTĚ()
    mobs.apply_effect(BLINDNESS, mobs.target(ALL_ENTITIES), 30, 255)
    mobs.apply_effect(STRENGTH, mobs.target(ALL_ENTITIES), 30, 3)
    mobs.spawn(VILLAGER, world(X2, -59, Z2))
    mobs.spawn(VILLAGER, world(X2, -59, Z2))
    mobs.spawn(VILLAGER, world(X2, -59, Z2))
    mobs.spawn(VILLAGER, world(X2, -59, Z2))
    mobs.spawn(VILLAGER, world(X2, -59, Z2))
player.on_chat("bludiste", on_on_chat2)

def on_on_chat3():
    mobs.give(mobs.target(RANDOM_PLAYER), DIAMOND_SWORD, 1)
    mobs.apply_effect(BLINDNESS, mobs.target(NEAREST_PLAYER), 10, 1)
player.on_chat("run", on_on_chat3)

def on_on_chat4():
    for index2 in range(20):
        jedna_cast_parkuru()
player.on_chat("parkur", on_on_chat4)

def jednacastdroperu():
    global X2, Y, Z2
    X2 = randint(-19, -9)
    Y = randint(-55, -25)
    Z2 = randint(-6, 3)
    blocks.place(COBWEB, world(X2, Y, Z2))
    blocks.place(COBWEB, world(X2, Y, Z2))
    player.say(":)")

def on_on_chat5():
    for index3 in range(40):
        jednacastdroperu()
player.on_chat("Droper", on_on_chat5)

Y = 0
Z2 = 0
X2 = 0
blocks.fill(AIR,
    world(-16, -57, 5),
    world(-8, -60, 36),
    FillOperation.REPLACE)
blocks.fill(WHITE_CONCRETE,
    world(-15, -60, 5),
    world(-9, -60, 35),
    FillOperation.REPLACE)
blocks.fill(WHITE_CONCRETE,
    world(-15, -57, 5),
    world(-9, -57, 35),
    FillOperation.REPLACE)
blocks.fill(WHITE_CONCRETE,
    world(-8, -59, 4),
    world(-8, -58, 35),
    FillOperation.REPLACE)
blocks.fill(WHITE_CONCRETE,
    world(-16, -59, 4),
    world(-16, -58, 35),
    FillOperation.REPLACE)