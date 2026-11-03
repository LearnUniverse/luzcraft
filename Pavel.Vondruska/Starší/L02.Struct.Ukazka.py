# L02.Struct.Ukazka.py obsahuje ukázku knihovny struktur a jejich generování do světa.
# Při spuštění se do světa uloží dvě struktury, které se následně dají generovat do světa.
# Při zadání "Build" se vygeneruje 30 struktur P_one a každá čtvrtá struktura bude P_two.

def Init_P_one():
    blocks.save_structure("P_one", world(-1, 0, -4), world(1, 2, -6))
    player.say("Library initialized")

def on_on_chat():
    generateToLibrary()
player.on_chat("Test", on_on_chat)

def generateToLibrary():
    Init_P_one()
    Init_P_Bridge()
def Load_P_one(Styl: str, Objekt: str):
    global buildCount
    if Styl == "":
        blocks.load_structure(Objekt, pos(0, 0, -3))
        buildCount += 1
        player.say("P_one at SIX")
    elif Styl == "random":
        randomizePos()
        blocks.load_structure(Objekt, pos(randX, randY, randZ))
        buildCount += 1
    else:
        pass
def randomizePos():
    global randX, randY, randZ
    randX = randint(0, 50)
    randY = randint(0, 50)
    randZ = randint(0, 50)

def on_on_chat2():
    for index in range(30):
        Load_P_one("random", "P_one")
        player.say("Build: " + str(buildCount))
        if buildCount % 4 == 0:
            Load_P_one("random", "P_two")
player.on_chat("Build", on_on_chat2)

def Init_P_Bridge():
    blocks.save_structure("P_two", world(3, 0, -4), world(9, 2, -5))
    player.say("Library initialized")
randZ = 0
randY = 0
randX = 0
buildCount = 0
hrac = ""
generateToLibrary()
buildCount = 0