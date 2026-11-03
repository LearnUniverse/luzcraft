# ============================================================
# MAX PARKUR - Minecraft Education Edition
# ============================================================
# POPIS:
#   Generátor parkurové dráhy - postupně vytváří platformy
#   (DIRT) ve směru osy X, s náhodným posunem v ose Z a
#   náhodným převýšením v ose Y mezi jednotlivými skoky.
#
# HLAVNÍ MECHANIKY:
#   - on_chat("run")    -> nastaví výchozí parametry podle
#                          pozice hráče a spustí generování
#   - Parkur(pocet)     -> smyčka, která pro každý level
#                          vytvoří platformu a posune pozici
#                          dál (X) a nahoru/dolů (Y)
#
# KLÍČOVÉ PROMĚNNÉ:
#   x/y/z                - aktuální pozice generování platformy
#   delka/sirka           - rozměry jedné platformy
#   Max_delka_air         - max. vzdálenost skoku mezi platformami
#   level_Pocet           - počet generovaných platforem (levelů)
#   y_je_bombove          - náhodná hodnota určující změnu výšky
# ============================================================


x = 0
y = 0
z = 0
delka = 0
sirka = 0
Max_delka_air = 0
level_Pocet = 0
y_je_bombove = 0
def nastav_promeni():
    global x, y, z, delka, sirka, Max_delka_air, level_Pocet
    x = player.position().get_value(Axis.X)
    y = player.position().get_value(Axis.Y)
    z = player.position().get_value(Axis.Z)
    delka = 2
    sirka = 2
    Max_delka_air = 10
    Max_delka_air = 10
    level_Pocet = 300

def on_on_chat():
    nastav_promeni()
    Parkur(level_Pocet)
player.on_chat("run", on_on_chat)

def Parkur(pocet_level: number):
    global x, y_je_bombove, y
    for index in range(pocet_level):
        blocks.fill(DIRT,
            world(x + randint(1, sirka), y - 1, z + randint(1, delka)),
            world(x - randint(1, sirka), y - 1, z - randint(1, delka)),
            FillOperation.HOLLOW)
        x += randint(6, Max_delka_air)
        y_je_bombove = randint(-3, 1)
        if y_je_bombove == -3:
            y += -3
        elif y_je_bombove == -2:
            y += -2
        elif y_je_bombove == -1:
            y += -1
        elif y_je_bombove == 0:
            y += 0
        else:
            y += 1