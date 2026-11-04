# tato jednoduchá hra funguje tak, že příkazem "run" se spustí generátor kuřat, 
# která se budou spawnovat každou sekundu. Když hráč zabije kuře, dostane diamant. 
# Hra se dá vypnout příkazem "run" znovu.

def on_forever():
    if X2 % 2 == 1:
        loops.pause(1000)
        mobs.spawn(CHICKEN, pos(0, 5, 0))
loops.forever(on_forever)

def on_mob_killed_chicken():
    if X2 % 2 == 1:
        mobs.give(mobs.target(LOCAL_PLAYER), DIAMOND, 1)
mobs.on_mob_killed(CHICKEN, on_mob_killed_chicken)

def on_on_chat():
    global X2
    X2 += 1
    gameplay.set_game_rule(MOB_LOOT, False)
player.on_chat("run", on_on_chat)

X2 = 0
X2 = 0