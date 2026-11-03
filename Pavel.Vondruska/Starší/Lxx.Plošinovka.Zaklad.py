# tato jednoduchá hra příkazem "game" spustí generátor plošinovky, 
# která se bude generovat každou sekundu. Když hráč zabije kuře, dostane diamant. 
# Hra se dá vypnout příkazem "game" znovu.


tntCount = 0
tntList: List[Position] = []
tntPos: Position = None
MaxStages = 0
SafeSpace = 0
MaxJump = 0
Max_delka_stage = 0
Max_sirka_stage = 0
Pos_X = 0
Pos_Y = 0
Pos_Z = 0
blockCesty = 0
pořadí = 0
Old_X = 0
Old_Y = 0
Old_Z = 0

def on_on_chat():
    global tntCount, tntPos
    tntCount = len(tntList)
    tntPos = tntList.shift()
    while tntCount >= 0:
        blocks.place(TNT, tntPos)
        blocks.place(REDSTONE_BLOCK,
            world(tntPos.get_value(Axis.X),
                tntPos.get_value(Axis.Y) + 1,
                tntPos.get_value(Axis.Z)))
        tntPos = tntList.shift()
        tntCount = len(tntList)
player.on_chat("tnts", on_on_chat)

def on_on_chat2():
    global MaxStages, SafeSpace, MaxJump, Max_delka_stage, Max_sirka_stage, Pos_X, Pos_Y, Pos_Z, blockCesty, Old_X, Old_Y, Old_Z, pořadí
    MaxStages = 10
    SafeSpace = 3
    MaxJump = 1
    Max_delka_stage = 5
    Max_sirka_stage = 5
    Pos_X = player.position().get_value(Axis.X)
    Pos_Y = player.position().get_value(Axis.Y)
    Pos_Z = player.position().get_value(Axis.Z)
    blockCesty = JACK_O_LANTERN
    blocks.fill(POLISHED_DIORITE,
        world(Pos_X - 5, Pos_Y - 1, Pos_Z - 7),
        world(Pos_X + 5, Pos_Y - 1, Pos_Z + 1),
        FillOperation.REPLACE)
    mobs.teleport_to_position(mobs.target(ALL_PLAYERS),
        world(Pos_X - 0, Pos_Y - 1, Pos_Z - 2))
    player.say("Blok start umístěn: " + "")
    Pos_Z += SafeSpace
    while pořadí <= MaxStages:
        Old_X = Pos_X
        Old_Y = Pos_Y
        Old_Z = Pos_Z
        Pos_X += randint(Max_sirka_stage * -1, Max_sirka_stage)
        Pos_Z += randint(1, Max_delka_stage)
        player.say("Pos_X" + ("" + str(Pos_X)) + " a old" + ("" + str(Old_X)))
        player.say("Pos_Y" + ("" + str(Pos_Y)) + " a old " + ("" + str(Old_Y)))
        player.say("Pos_Z" + ("" + str(Pos_Z)) + " a old " + ("" + str(Old_Z)))
        blocks.fill(blockCesty,
            world(Old_X, Old_Y, Old_Z),
            world(Pos_X, Pos_Y, Pos_Z),
            FillOperation.REPLACE)
        tntList.append(world(Old_X, Old_Y + 1, Old_Z))
        Pos_Z += randint(1, SafeSpace)
        Pos_Y += randint(-1, MaxJump)
        player.say("Plošina: " + ("" + str(pořadí)))
        pořadí += 1
    player.say("Plošinovka hotova. Celkem stages: " + ("" + str(pořadí)))
player.on_chat("Game", on_on_chat2)
