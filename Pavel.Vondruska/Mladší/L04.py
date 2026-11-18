# ============================================================
# CIRCLE TRACKER - Minecraft Education Edition
# ============================================================
# POPIS:
#   Sada diagnostických/herních příkazů, které vypisují
#   aktuální pozici hráče do chatu a volitelně kolem něj
#   vykreslí magentový kruh z vlny (MAGENTA_WOOL). Varianta
#   "Where4" navíc vykresluje sérii kruhů stoupajících nahoru
#   s náhodným posunem v X/Z mezi jednotlivými kruhy.
#
# HLAVNÍ MECHANIKY:
#   - on_chat("Where4") -> vypíše pozici, vykreslí sérii
#                          kruhů (OUTLINE) stoupajících nahoru,
#                          každý náhodně posunutý v X/Z
#   - on_chat("Where3") -> vypíše pozici a vykreslí jeden
#                          magentový kruh kolem hráče
#   - on_chat("Where")  -> pouze vypíše aktuální pozici hráče
#                          do chatu (bez vykreslení kruhu)
#
# KLÍČOVÉ PROMĚNNÉ:
#   X2/Y/Z2             - aktuální souřadnice hráče použité
#                          pro vykreslení/oznámení pozice
# ============================================================

X2 = 0
Y = 0
Z2 = 0

def on_on_chat():
    global X2, Y, Z2
    X2 = player.position().get_value(Axis.X)
    Y = player.position().get_value(Axis.Y)
    Z2 = player.position().get_value(Axis.Z)
    player.say("X " + ("" + str(X2)) + " Y " + ("" + str(Y)) + " Z " + ("" + str(Z2)))
    shapes.circle(MAGENTA_WOOL,
        world(X2, Y + 5, Z2 + 5),
        5,
        Axis.Z,
        ShapeOperation.OUTLINE)
player.on_chat("Where2", on_on_chat)

def on_on_chat2():
    global X2, Y, Z2
    X2 = player.position().get_value(Axis.X)
    Y = player.position().get_value(Axis.Y)
    Z2 = player.position().get_value(Axis.Z)
    player.say("X " + ("" + str(X2)) + " Y " + ("" + str(Y)) + " Z " + ("" + str(Z2)))
    for index in range(3):
        shapes.circle(PURPLE_WOOL,
            world(X2, Y, Z2),
            randint(5, 10),
            Axis.Y,
            ShapeOperation.OUTLINE)
        X2 = X2 + randint(1, 6)
        Y = Y + randint(10, 20)
        Z2 = Z2 + randint(1, 10)
    player.teleport(world(X2, Y + 10, Z2))
    mobs.give(mobs.target(LOCAL_PLAYER), ELYTRA, 1)
player.on_chat("Where5", on_on_chat2)

def on_on_chat3():
    global X2, Y, Z2
    X2 = player.position().get_value(Axis.X)
    Y = player.position().get_value(Axis.Y)
    Z2 = player.position().get_value(Axis.Z)
    player.say("X " + ("" + str(X2)) + " Y " + ("" + str(Y)) + " Z " + ("" + str(Z2)))
    for index2 in range(10):
        shapes.circle(LIME_WOOL,
            world(X2, Y, Z2),
            5,
            Axis.Y,
            ShapeOperation.OUTLINE)
        X2 = X2 + randint(0, 4)
        Y = Y + randint(5, 10)
        Z2 = Z2 + randint(0, 4)
player.on_chat("Where4", on_on_chat3)

def on_on_chat4():
    global X2, Y, Z2
    X2 = player.position().get_value(Axis.X)
    Y = player.position().get_value(Axis.Y)
    Z2 = player.position().get_value(Axis.Z)
    player.say("X " + ("" + str(X2)) + " Y " + ("" + str(Y)) + " Z " + ("" + str(Z2)))
    shapes.circle(MAGENTA_WOOL,
        world(X2, Y, Z2),
        5,
        Axis.Y,
        ShapeOperation.OUTLINE)
player.on_chat("Where3", on_on_chat4)

def on_on_chat5():
    global X2, Y, Z2
    X2 = player.position().get_value(Axis.X)
    Y = player.position().get_value(Axis.Y)
    Z2 = player.position().get_value(Axis.Z)
    player.say("X " + ("" + str(X2)) + " Y " + ("" + str(Y)) + " Z " + ("" + str(Z2)))
player.on_chat("Where", on_on_chat5)
