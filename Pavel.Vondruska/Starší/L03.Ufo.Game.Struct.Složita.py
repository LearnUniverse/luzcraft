# ============================================================
# UFO SKY TOWER - Minecraft Education Edition
# ============================================================
# POPIS:
#   Hra generuje nad hráčem řetězec struktur (UFO a krychlí)
#   stoupajících do výšky s náhodným vodorovným posunem.
#   Hráč tak musí sledovat/dohánět postupně stoupající cestu
#   složenou z předpřipravených struktur.
#
# HLAVNÍ MECHANIKY:
#   - on_chat("game_kr")  -> vygeneruje num12 kopií struktury
#                          "P_ufo" nad hráčem, každá o 5 výš
#                          a náhodně posunutá (-10..10) v X/Z
#   - on_chat("game_ufo") -> stejné jako výše, ale s menším
#                          rozptylem posunu (-5..5) a bez
#                          chatového oznámení
#   - on_chat("Test")     -> zavolá pomocnou funkci pro
#                          generování do knihovny struktur
#   - on_chat("game_kr2") -> kombinovaná verze, střídavě
#                          generuje "P_ufo" a "P_one" struktury
#   - Init_P_one()        -> uloží aktuální oblast jako
#                          strukturu "P_one" (nástroj pro
#                          přípravu obsahu, ne pro hráče)
#
# KLÍČOVÉ PROMĚNNÉ:
#   pX/pY/pZ             - aktuální pozice generování struktury,
#                          postupně se posouvá nahoru a do stran
# ============================================================


def on_on_chat(num12):
    global pX, pY, pZ
    pX = player.position().get_value(Axis.X)
    pY = player.position().get_value(Axis.Y)
    pZ = player.position().get_value(Axis.Z)
    for index in range(num12):
        player.say(num12)
        blocks.load_structure("P_ufo", world(pX, pY + 0, pZ))
        pY += 5
        pX += randint(-10, 10)
        pZ += randint(-10, 10)
player.on_chat("game_kr", on_on_chat)

def Init_P_one():
    blocks.save_structure("P_one", world(-1, 0, -4), world(1, 2, -6))
    player.say("Cube initialized")

def on_on_chat2(num14):
    global pX, pY, pZ
    pX = player.position().get_value(Axis.X)
    pY = player.position().get_value(Axis.Y)
    pZ = player.position().get_value(Axis.Z)
    for index2 in range(num14):
        blocks.load_structure("P_ufo", world(pX, pY + 0, pZ))
        pY += 5
        pX += randint(-5, 5)
        pZ += randint(-5, 5)
player.on_chat("game_ufo", on_on_chat2)

def on_on_chat3():
    generateToLibrary()
player.on_chat("Test", on_on_chat3)

def on_on_chat4(num13):
    global pX, pY, pZ
    pX = player.position().get_value(Axis.X)
    pY = player.position().get_value(Axis.Y)
    pZ = player.position().get_value(Axis.Z)
    for index3 in range(num13):
        blocks.load_structure("P_ufo", world(pX, pY + 0, pZ))
        pX += randint(-10, 10)
        pZ += randint(-10, 10)
        blocks.load_structure("P_one", world(pX, pY + 2, pZ))
        pX += randint(-10, 10)
        pZ += randint(-10, 10)
        blocks.load_structure("P_two", world(pX, pY + 1, pZ))
        pY += 5
player.on_chat("game_ufo2", on_on_chat4)

def zasadStrom(naX: number, naY: number, naZ: number, strom: str):
    global prikazStrom
    prikazStrom = "/place feature minecraft:" + strom + " " + ("" + str(naX)) + " " + ("" + str(naY)) + " " + ("" + str(naZ))
    blocks.place(GRASS, world(naX, naY - 1, naZ))
    player.execute(prikazStrom)
def generateToLibrary():
    Init_P_one()
    Init_P_Bridge()

def on_on_chat5():
    global poc, pX, pY, pZ
    poc = 0
    for index4 in range(4):
        poc += 1
        pX = player.position().get_value(Axis.X)
        pY = player.position().get_value(Axis.Y)
        pZ = player.position().get_value(Axis.Z)
        player.say(poc)
        zasadStrom(pX, pY * poc, pZ, "cherry_tree_feature ")
player.on_chat("x", on_on_chat5)

def on_on_chat6():
    Init_P_Ufo()
player.on_chat("init_ufo", on_on_chat6)

def on_on_chat7():
    blocks.fill(WOOL,
        world(-1, 0, -4),
        world(1, 2, -6),
        FillOperation.REPLACE)
    blocks.fill(WOOL,
        world(3, 0, -4),
        world(9, 2, -5),
        FillOperation.REPLACE)
    player.teleport(world(0, 0, 0))
player.on_chat("HelpInit", on_on_chat7)

def Load_P_one(Styl: str, Objekt: str):
    global levelBuildCount
    if Styl == "":
        blocks.load_structure(Objekt, pos(0, 0, -3))
        levelBuildCount += 1
        player.say("P_one at SIX")
    elif Styl == "random":
        randomizePos()
        blocks.load_structure(Objekt, pos(randX, randY, randZ))
        levelBuildCount += 1
    else:
        pass

def on_on_chat8(num122):
    global pX, pY, pZ, levelBuildCount, levX, levY, levZ
    pX = player.position().get_value(Axis.X)
    pY = player.position().get_value(Axis.Y)
    pZ = player.position().get_value(Axis.Z)
    levelBuildCount = num122
    for index5 in range(num122):
        levelBuildCount += -1
        player.say("Loading game :" + ("" + str(levelBuildCount)))
        blocks.load_structure("P_ufo", world(pX, pY + 0, pZ))
        if levelBuildCount == 0:
            levX = pX
            levY = pY
            levZ = pZ
        for index6 in range(num122):
            pX += randint(-4, 4)
            pZ += randint(-4, 4)
            blocks.load_structure("P_one", world(pX, pY + 2, pZ))
            zasadStrom(pX, pY + 3, pZ, "cherry_tree_feature ")
            pX += randint(-4, 4)
            pZ += randint(-4, 4)
            blocks.load_structure("P_two", world(pX, pY + 1, pZ))
            zasadStrom(pX, pY + 3, pZ, "cherry_tree_feature ")
        pY += 5
        pX += randint(-10, 10)
        pZ += randint(-10, 10)
    mobs.teleport_to_position(mobs.target(ALL_PLAYERS),
        world(levX + 10, levY + 3, levZ + 14))
    player.say("Game started" + "...")
player.on_chat("game_ufo5", on_on_chat8)

def randomizePos():
    global randX, randY, randZ
    randX = randint(0, 50)
    randY = randint(0, 50)
    randZ = randint(0, 50)

def on_on_chat9(num123):
    global pX, pY, pZ, levelBuildCount
    num1222 = 0
    pX = player.position().get_value(Axis.X)
    pY = player.position().get_value(Axis.Y)
    pZ = player.position().get_value(Axis.Z)
    levelBuildCount = num1222
    for index7 in range(num123):
        levelBuildCount += -1
        player.say("Loading game :" + ("" + str(levelBuildCount)))
        blocks.load_structure("P_ufo", world(pX, pY + 0, pZ))
        for index8 in range(num123):
            pX += randint(-4, 4)
            pZ += randint(-4, 4)
            blocks.load_structure("P_one", world(pX, pY + 2, pZ))
            pX += randint(-4, 4)
            pZ += randint(-4, 4)
            blocks.load_structure("P_two", world(pX, pY + 1, pZ))
        pY += 5
        pX += randint(-10, 10)
        pZ += randint(-10, 10)
player.on_chat("game_ufo3", on_on_chat9)

def Init_P_Ufo():
    blocks.save_structure("P_ufo", world(-52, 0, -54), world(-74, 2, -79))
    player.say("Ufo initialized")

def on_on_chat10():
    for index9 in range(30):
        Load_P_one("random", "P_one")
        player.say("Build: " + ("" + str(levelBuildCount)))
        if levelBuildCount % 4 == 0:
            Load_P_one("random", "P_two")
player.on_chat("Build", on_on_chat10)

def on_on_chat11():
    global pX, pY, pZ
    pX = player.position().get_value(Axis.X)
    pY = player.position().get_value(Axis.Y)
    pZ = player.position().get_value(Axis.Z)
    pZ += 15
    shapes.circle(POLISHED_DIORITE,
        world(pX, pY + 0, pZ),
        10,
        Axis.Y,
        ShapeOperation.REPLACE)
    shapes.circle(LIME_WOOL,
        world(pX, pY + 1, pZ),
        11,
        Axis.Y,
        ShapeOperation.REPLACE)
    shapes.circle(POLISHED_DIORITE,
        world(pX, pY + 2, pZ),
        10,
        Axis.Y,
        ShapeOperation.REPLACE)
    blocks.save_structure("P_ufo",
        world(pX - 11, pY, pZ - 11),
        world(pX + 11, pY + 2, pZ + 11))
    player.say("Ufo initialized")
player.on_chat("kr", on_on_chat11)

def on_on_chat12(num12222):
    global pX, pY, pZ, levelBuildCount, levX, levY, levZ
    pX = player.position().get_value(Axis.X)
    pY = player.position().get_value(Axis.Y)
    pZ = player.position().get_value(Axis.Z)
    levelBuildCount = num12222
    for index10 in range(num12222):
        levelBuildCount += -1
        player.say("Loading game :" + ("" + str(levelBuildCount)))
        blocks.load_structure("P_ufo", world(pX, pY + 0, pZ))
        if levelBuildCount == 0:
            levX = pX
            levY = pY
            levZ = pZ
        for index11 in range(num12222):
            pX += randint(-4, 4)
            pZ += randint(-4, 4)
            blocks.load_structure("P_one", world(pX, pY + 2, pZ))
            pX += randint(-4, 4)
            pZ += randint(-4, 4)
            blocks.load_structure("P_two", world(pX, pY + 1, pZ))
        pY += 5
        pX += randint(-10, 10)
        pZ += randint(-10, 10)
    mobs.teleport_to_position(mobs.target(ALL_PLAYERS),
        world(levX + 10, levY + 3, levZ + 14))
    player.say("Game started" + "...")
player.on_chat("game_ufo4", on_on_chat12)

def Init_P_Bridge():
    blocks.save_structure("P_two", world(3, 0, -4), world(9, 2, -5))
    player.say("Brigde initialized")
levZ = 0
levY = 0
levX = 0
randZ = 0
randY = 0
randX = 0
poc = 0
prikazStrom = ""
pZ = 0
pY = 0
pX = 0
levelBuildCount = 0
hrac = ""
generateToLibrary()
levelBuildCount = 0
Init_P_Ufo()