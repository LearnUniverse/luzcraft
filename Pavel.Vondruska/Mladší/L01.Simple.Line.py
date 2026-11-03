# když uživatel napíše "run" do chatu, vygeneruje se náhodná linie z magenta glazované terakoty, 
# která se bude prodlužovat směrem nahoru

def on_on_chat(steps):
    global NextX, NextY, NextZ, MaxDestiny
    NextX = player.position().get_value(Axis.X)
    NextY = player.position().get_value(Axis.Y)
    NextZ = player.position().get_value(Axis.Z)
    while MaxDestiny < steps:
        NextZ += 1
        player.say(MaxDestiny)
        NextX = NextX + randint(-1, 1)
        NextY = NextY + randint(-1, 1)
        blocks.place(MAGENTA_GLAZED_TERRACOTTA, world(NextX, NextY, NextZ))
        MaxDestiny += 1
player.on_chat("run", on_on_chat)

NextZ = 0
NextY = 0
NextX = 0
MaxDestiny = 0
MaxDestiny = 0