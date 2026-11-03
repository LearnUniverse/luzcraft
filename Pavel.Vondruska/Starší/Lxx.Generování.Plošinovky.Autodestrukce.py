# Celý kód funguje tak, že po zadání příkazu "Game" se spustí funkce, která nastaví parametry hry, 
# vytvoří startovní blok a vygeneruje několik plošin. 
# Poté začne odpočítávání a postupně se zničí plošiny pomocí TNT. 
# Při zadání příkazu "bomb" se umístí TNT a červený kámen pro jeho aktivaci.


MaxStages = 0
SafeSpace = 0
MaxJump = 0
Max_delka_stage = 0
Max_sirka_stage = 0
Pos_X = 0
Pos_Y = 0
Pos_Z = 0
plateMaterial = 0
circleMat = 0
kouleMat = 0
stageStep = 0
Old_X = 0
Old_Y = 0
Old_Z = 0
tntList: List[Position] = []
timerSek = 0
tntCount = 0
tntPos: Position = None
def bombIt():
    blocks.place(TNT, pos_camera(0, 50, 15))
    blocks.place(REDSTONE_BLOCK, pos_camera(0, 49, 15))
    loops.pause(1000)
    blocks.place(AIR, pos_camera(0, 49, 15))
def SetupGame():
    global MaxStages, SafeSpace, MaxJump, Max_delka_stage, Max_sirka_stage, Pos_X, Pos_Y, Pos_Z, plateMaterial, circleMat, kouleMat
    MaxStages = 5
    SafeSpace = 3
    MaxJump = 1
    Max_delka_stage = 5
    Max_sirka_stage = 5
    Pos_X = player.position().get_value(Axis.X)
    Pos_Y = player.position().get_value(Axis.Y)
    Pos_Z = player.position().get_value(Axis.Z)
    plateMaterial = LIME_GLAZED_TERRACOTTA
    circleMat = PURPLE_WOOL
    kouleMat = ORANGE_WOOL
def GenerateLevelPlates():
    global Old_X, Old_Y, Old_Z, Pos_X, Pos_Z, Pos_Y, stageStep
    while stageStep <= MaxStages:
        Old_X = Pos_X
        Old_Y = Pos_Y
        Old_Z = Pos_Z
        Pos_X += randint(Max_sirka_stage * -1, Max_sirka_stage)
        Pos_Z += randint(1, Max_delka_stage)
        blocks.fill(plateMaterial,
            world(Old_X, Old_Y, Old_Z),
            world(Pos_X, Pos_Y, Pos_Z),
            FillOperation.REPLACE)
        shapes.circle(circleMat,
            world(Old_X, Old_Y, Old_Z),
            5,
            Axis.Z,
            ShapeOperation.OUTLINE)
        shapes.sphere(kouleMat,
            world(Old_X, Old_Y, Old_Z),
            2,
            ShapeOperation.HOLLOW)
        tntList.append(world(Old_X, Old_Y + 1, Old_Z))
        Pos_Z += randint(1, SafeSpace)
        Pos_Y += randint(-1, MaxJump)
        player.say("Plošina: " + ("" + str(stageStep)))
        stageStep += 1
    player.say("Plošinovka hotova. Celkem stages: " + ("" + str(stageStep)))
def countDownAndDestroy(inTimerSek: number):
    global timerSek, tntCount, tntPos
    timerSek = inTimerSek
    tntCount = len(tntList)
    tntPos = tntList.shift()
    while tntCount >= 0:
        while timerSek != 0:
            loops.pause(1000)
            timerSek = timerSek - 1
        blocks.place(TNT, tntPos)
        blocks.place(REDSTONE_BLOCK,
            world(tntPos.get_value(Axis.X),
                tntPos.get_value(Axis.Y) + 1,
                tntPos.get_value(Axis.Z)))
        blocks.place(REDSTONE_BLOCK,
            world(tntPos.get_value(Axis.X),
                tntPos.get_value(Axis.Y) + 49,
                tntPos.get_value(Axis.Z) - 2))
        blocks.place(TNT,
            world(tntPos.get_value(Axis.X),
                tntPos.get_value(Axis.Y) + 50,
                tntPos.get_value(Axis.Z) - 2))
        loops.pause(1200)
        blocks.place(AIR,
            world(tntPos.get_value(Axis.X),
                tntPos.get_value(Axis.Y) + 49,
                tntPos.get_value(Axis.Z) - 2))
        tntPos = tntList.shift()
        tntCount = len(tntList)
        timerSek = inTimerSek
def BuildStartPlace():
    global Pos_Z
    blocks.place(POLISHED_DIORITE, world(Pos_X, Pos_Y - 1, Pos_Z))
    player.say("Blok start umístěn: " + "")
    Pos_Z += SafeSpace

def on_on_chat():
    SetupGame()
    BuildStartPlace()
    GenerateLevelPlates()
    countDownAndDestroy(5)
player.on_chat("Game", on_on_chat)

def on_on_chat2():
    bombIt()
player.on_chat("bomb", on_on_chat2)
