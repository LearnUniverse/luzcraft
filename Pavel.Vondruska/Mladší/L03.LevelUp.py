# ============================================================
# ZOMBIE LEVEL UP - Minecraft Education Edition
# ============================================================
# POPIS:
#   Vlnová (wave) survival hra proti zombie. Každých 5 sekund
#   se spawnuje jeden zombie. Jakmile hráč zabije dostatek
#   zombíků, postoupí na další level a obtížnost se zvýší -
#   spawne se více zombíků najednou podle aktuálního levelu.
#
# HLAVNÍ MECHANIKY:
#   - on_forever()       -> každých 5s vyspawnuje 1 zombíka
#   - on_forever2()      -> kontroluje postup levelem; po
#                          dosažení potřebného počtu zabití
#                          (level + 10) vyspawnuje "level" zombíků
#                          a zvýší level o 1
#   - on_mob_killed()    -> při zabití zombíka zvýší počítadlo
#                          zabití a oznámí ho v chatu
#
# KLÍČOVÉ PROMĚNNÉ:
#   pocetZabiti          - aktuální počet zabitých zombíků
#                          v rámci levelu
#   level                - aktuální úroveň hráče (obtížnost)
# ============================================================


def on_forever():
    mobs.spawn(mobs.monster(ZOMBIE), pos(0, 0, 5))
    loops.pause(5000)
loops.forever(on_forever)

def on_forever2():
    global pocetZabiti, level
    if pocetZabiti >= level + 10:
        pocetZabiti = 0
        for index in range(level):
            mobs.spawn(mobs.monster(ZOMBIE), pos(0, 0, 5))
        player.say("Level: " + str(level))
        level += 1
loops.forever(on_forever2)

def on_mob_killed():
    global pocetZabiti
    pocetZabiti += 1
    player.say("Zabiti" + str(pocetZabiti))
mobs.on_mob_killed(mobs.monster(ZOMBIE), on_mob_killed)

pocetZabiti = 0
level = 0
gameplay.set_difficulty(EASY)
gameplay.set_game_mode(SURVIVAL, mobs.target(ALL_PLAYERS))
level = 1
pocetZabiti = 0