# Generátor chodeb (Minecraft MakeCode, Python)
#   Z uložené struktury "main hall" (7x6x9 bloků) skládá náhodně se větvící chodbu.
#   Použití: v chatu napsat "run" a počet kroků (např. "run 10").
#   Každý krok:
#     - náhodně zatočí vlevo (smer -1), pokračuje rovně, nebo zatočí vpravo (smer +1)
#     - posune se o 8 bloků ve směru smer % 4 (0 = +z, 1 = +x, 2 = -z, 3 = -x)
#       a vloží sekci chodby natočenou o 0/90/180/270 stupňů
#   Po dokončení hráč dostane zprávu "hotovo".
#   Poznámky:
#     - struktura "main hall" se při každém spuštění programu znovu uloží z world(-370,64,254)..(-364,69,246),
#       tam musí stát vzorová chodba
#     - souřadnice x, z se při každém "run" nulují a pos() je relativní k hráči, takže chodba začíná u něj
#     - smer se mezi spuštěními "run" neresetuje, další chodba tedy začne ve směru, kde skončila předchozí
def posun_smerem():
    global z, x
    if smer % 4 == 0:
        z += 4
        blocks.load_structure("main hall", pos(x - 3, -1, z))
        z += 4
    if smer % 4 == 1:
        x += 4
        blocks.load_structure("main hall", pos(x, -1, z - 3), DEGREES90)
        x += 4
    if smer % 4 == 2:
        z += -4
        blocks.load_structure("main hall", pos(x - 3, -1, z - 8), DEGREES180)
        z += -4
    if smer % 4 == 3:
        x += -4
        blocks.load_structure("main hall", pos(x - 8, -1, z - 3), DEGREES270)
        x += -4

def on_on_chat(pocetKroku):
    global x, z, nahodna, smer
    x = 0
    z = 0
    for index in range(pocetKroku):
        nahodna = randint(1, 3)
        if nahodna == 1:
            smer += -1
            posun_smerem()
        if nahodna == 2:
            posun_smerem()
        if nahodna == 3:
            smer += 1
            posun_smerem()
    player.say("hotovo")
player.on_chat("run", on_on_chat)

nahodna = 0
z = 0
x = 0
smer = 0
smer = 100
x = 0
z = 0
blocks.save_structure("main hall", world(-370, 64, 254), world(-364, 69, 246))