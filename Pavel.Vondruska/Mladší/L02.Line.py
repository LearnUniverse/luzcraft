# celý kód funguje tak, že po zadání 
#  Go se vytvoří 45 bloků magenta, 
#  po zadání Go2 se vytvoří 45 bloků magenta a nad nimi se spawnou zombíci, 
#  po zadání Go3 se vytvoří 45 bloků světle modré a nad nimi se spawnou creepeři, 
#  po zadání run X se vytvoří X bloků magenta a hráč uvidí číslo kolik bloků bylo vytvořeno

NextX = 0
NextY = 0
NextZ = 0
MaxDestiny = 0

def on_on_chat():
    global NextX, NextY, NextZ
    NextX = player.position().get_value(Axis.X)
    NextY = player.position().get_value(Axis.Y)
    NextZ = player.position().get_value(Axis.Z)
    for index in range(45):
        NextZ = NextZ + 2
        blocks.place(MAGENTA_GLAZED_TERRACOTTA, world(NextX, NextY, NextZ))
player.on_chat("Go", on_on_chat)

def on_on_chat2():
    global NextX, NextY, NextZ
    gameplay.set_difficulty(EASY)
    NextX = player.position().get_value(Axis.X)
    NextY = player.position().get_value(Axis.Y)
    NextZ = player.position().get_value(Axis.Z)
    for index2 in range(45):
        NextZ = NextZ + 2
        NextY = NextY + randint(-1, 1)
        NextX = NextX + randint(-1, 1)
        blocks.place(LIGHT_BLUE_CONCRETE, world(NextX, NextY, NextZ))
        mobs.spawn(mobs.monster(CREEPER), world(NextX, NextY + 1, NextZ))
player.on_chat("Go3", on_on_chat2)

def on_on_chat3():
    global NextX, NextY, NextZ
    gameplay.set_difficulty(EASY)
    NextX = player.position().get_value(Axis.X)
    NextY = player.position().get_value(Axis.Y)
    NextZ = player.position().get_value(Axis.Z)
    for index3 in range(45):
        NextZ = NextZ + 2
        blocks.place(MAGENTA_GLAZED_TERRACOTTA, world(NextX, NextY, NextZ))
        mobs.spawn(mobs.monster(ZOMBIE), world(NextX, NextY + 1, NextZ))
player.on_chat("Go2", on_on_chat3)

def on_on_chat4(steps):
    global NextX, NextY, NextZ, MaxDestiny
    NextX = player.position().get_value(Axis.X)
    NextY = player.position().get_value(Axis.Y)
    NextZ = player.position().get_value(Axis.Z)
    while MaxDestiny < steps:
        NextZ += 1
        player.say(MaxDestiny)
        NextX = NextX + randint(-1, 1)
        blocks.place(MAGENTA_GLAZED_TERRACOTTA, world(NextX, NextY, NextZ))
        MaxDestiny += 1
player.on_chat("run", on_on_chat4)
