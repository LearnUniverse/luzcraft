# ============================================================
# ORE RUSH SURVIVAL - Minecraft Education Edition
# ============================================================
# POPIS:
#   Survival/mining minihra. Po spuštění chatem "HRA" se
#   vytvoří kamenná jeskyně/dolovací oblast, do které se
#   náhodně rozmístí rudy (uhlí, železo, zlato, diamant,
#   lapis) a 20 domků. Po uplynutí časového limitu (5 min)
#   se na hráče vyspawnuje vlna nepřátel (Ravager, Evoker,
#   Vindicator) jako finální boss fight.
#
# HLAVNÍ MECHANIKY:
#   - on_chat("HRA")    -> vygeneruje kamenný blok oblasti,
#                          naplní ho rudami, postaví 20 domků,
#                          po pauze 300000 ticků spawne
#                          nepřátelskou vlnu
#   - domek()           -> vygeneruje jeden domek (externí fce)
#   - uhlí()            -> rozmístí 200 kusů COAL_ORE náhodně
#                          v oblasti
#   - źelezo()          -> rozmístí 200 kusů IRON_ORE náhodně
#                          v oblasti
#   - zlato()           -> rozmístí zlatou rudu (externí fce)
#   - diamanti()        -> rozmístí diamantovou rudu (externí fce)
#   - lapiz()           -> rozmístí lapis rudu (externí fce)
#   - on_forever()      -> udržuje LOG_OAK blok na pozici
#                          (10, 0, 10), pokud zmizí, znovu ho
#                          umístí
#
# KLÍČOVÉ PROMĚNNÉ:
#   oblast souřadnic     - X: -12 až -23, Y: 0 až 25,
#                          Z: -16 až -29 (dolovací prostor)
# ============================================================

def on_on_chat():
    blocks.fill(STONE,
        world(-12, 0, -16),
        world(-23, 25, -29),
        FillOperation.REPLACE)
    for index in range(20):
        domek()
    uhlí()
    źelezo()
    zlato()
    diamanti()
    lapiz()
    loops.pause(300000)
    player.say(":)")
    mobs.spawn(mobs.monster(RAVAGER), world(30, 0, 30))
    mobs.spawn(mobs.monster(RAVAGER), world(30, 0, 30))
    for index2 in range(5):
        mobs.spawn(mobs.monster(EVOKER), world(30, 0, 30))
    for index3 in range(5):
        mobs.spawn(mobs.monster(VINDICATOR), world(30, 0, 30))
player.on_chat("HRA", on_on_chat)

def źelezo():
    for index4 in range(200):
        blocks.place(IRON_ORE,
            world(randint(-12, -23), randint(0, 25), randint(-16, -29)))
def uhlí():
    for index5 in range(200):
        blocks.place(COAL_ORE,
            world(randint(-12, -23), randint(0, 25), randint(-16, -29)))

def on_forever():
    if not (blocks.test_for_block(LOG_OAK, world(10, 0, 10))):
        blocks.place(LOG_OAK, world(10, 0, 10))
        mobs.give(mobs.target(ALL_PLAYERS), ARROW, 1)
loops.forever(on_forever)

def on_forever2():
    if not (blocks.test_for_block(WOOL, world(6, 0, 10))):
        blocks.place(WOOL, world(6, 0, 10))
        mobs.give(mobs.target(ALL_PLAYERS), COOKED_BEEF, 1)
loops.forever(on_forever2)

def domek():
    blocks.save_structure("domek", world(0, 3, -12), world(2, -5, -10))
    blocks.load_structure("domek", world(randint(0, 300), -2, randint(0, 300)))
def zlato():
    for index6 in range(100):
        blocks.place(GOLD_ORE,
            world(randint(-12, -23), randint(0, 25), randint(-16, -29)))
def lapiz():
    for index7 in range(100):
        blocks.place(LAPIS_ORE,
            world(randint(-12, -23), randint(0, 25), randint(-16, -29)))
def diamanti():
    for index8 in range(50):
        blocks.place(DIAMOND_ORE,
            world(randint(-12, -23), randint(0, 25), randint(-16, -29)))

def on_mob_killed_chicken():
    pass
mobs.on_mob_killed(CHICKEN, on_mob_killed_chicken)
