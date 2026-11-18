# ============================================================
# Generate.Massive.Tree.FCN.py - "MOHUTNÝ DUB"
# ============================================================
# POPIS:
#   Vygeneruje masivní (procedurální) strom s tlustým kmenem,
#   větvemi různé tloušťky a sklonu a korunou z listí. Strom
#   je generován pomocí zásobníkového (stack-based) algoritmu,
#   kde se každá větev rozděluje na další podvětve s menší
#   tloušťkou, náhodným sklonem a natočením. Silnější průřezy
#   (kmen, hlavní větve) jsou automaticky zaobleny, tenčí
#   větve jsou tvořeny jedním blokem.
#
# POUŽITÍ:
#   Zavolá se jednou pro vygenerování celého stromu na
#   zadaných souřadnicích. Funkce interně využívá zásobníky
#   (zasobnik_x/y/z/delka/sklon/natoceni/hloubka/tloustka)
#   pro simulaci rekurzivního větvení bez nutnosti skutečné
#   rekurze (kvůli omezením prostředí).
#
#   Příklad:
#       generate_massive_tree(0, 60, 0, 8, 20)
#
# PARAMETRY:
#   startX/startY/startZ - souřadnice paty kmene (kde strom
#                          začíná růst, světové souřadnice)
#   startTloustka        - počáteční tloušťka kmene (např. 8)
#   startDelka           - počáteční délka kmene (výška před
#                          prvním větvením)
#
# KLÍČOVÉ PROMĚNNÉ:
#   zasobnik_*           - zásobníky uchovávající parametry
#                          jednotlivých dosud nezpracovaných
#                          větví (pozice, délka, sklon,
#                          natočení, hloubka větvení, tloušťka)
#   idx                  - aktuální index zpracovávané větve
#                          v zásobníku
#
# NÁVRATOVÁ HODNOTA:
#   None
# ============================================================


d = 0
p1 = 0
p2 = 0
U1 = 0
U2 = 0
U3 = 0
sirka = 0
zasobnik_x: List[number] = []
zasobnik_y: List[number] = []
zasobnik_z: List[number] = []
zasobnik_delka: List[number] = []
zasobnik_sklon: List[number] = []
zasobnik_natoceni: List[number] = []
zasobnik_hloubka: List[number] = []
zasobnik_tloustka: List[number] = []
idx = 0
def vykresli_prurez(bx: number, by: number, bz: number, tloustka: number):
    global d, p1, p2
    d = Math.round(tloustka)
    if d <= 1:
        blocks.place(LOG_OAK, world(bx, by, bz))
        return
    p1 = Math.floor((d - 1) / 2)
    p2 = Math.ceil((d - 1) / 2)
    if d <= 3:
        blocks.fill(LOG_OAK,
            world(bx - p1, by - p1, bz - p1),
            world(bx + p2, by + p2, bz + p2),
            FillOperation.REPLACE)
    else:
        # Zaoblený průřez kmene a silných větví
        blocks.fill(LOG_OAK,
            world(bx - p1 + 1, by - p1, bz - p2),
            world(bx + p2 - 1, by + p2, bz + p1),
            FillOperation.REPLACE)
        blocks.fill(LOG_OAK,
            world(bx - p2, by - p1, bz - p1 + 1),
            world(bx + p1, by + p2, bz + p2 - 1),
            FillOperation.REPLACE)

def on_on_chat2():
    global U1, U2, U3
    U1 = player.position().get_value(Axis.X)
    U2 = player.position().get_value(Axis.Y)
    U3 = player.position().get_value(Axis.Z)
    vygeneruj_strom(6,
        U1 + randint(-20, 20),
        U2 + randint(-5, 0),
        U3 + randint(-20, 20))
player.on_chat("Strom", on_on_chat2)

def on_on_chat(sirka2: number, x: number, y: number, z: number):
    if sirka2 <= 0:
        sirka2 = 6
    # Pokud nezadáš souřadnice (zůstanou 0, 0, 0), postaví se strom 18 bloků před hráčem
    if x == 0 and y == 0 and z == 0:
        pozice = player.position()
        x = pozice.get_value(Axis.X) + 18
        y = pozice.get_value(Axis.Y)
        z = pozice.get_value(Axis.Z)
    vygeneruj_strom(sirka2, x, y, z)
def postav_listi(cx: number, cy: number, cz: number):
    # Shluk listí na konci větviček (FillOperation.KEEP nepoškodí dřevo větví)
    blocks.fill(LEAVES_OAK,
        world(cx - 3, cy - 1, cz - 2),
        world(cx + 3, cy + 2, cz + 2),
        FillOperation.KEEP)
    blocks.fill(LEAVES_OAK,
        world(cx - 2, cy - 1, cz - 3),
        world(cx + 2, cy + 2, cz + 3),
        FillOperation.KEEP)
    blocks.fill(LEAVES_OAK,
        world(cx - 2, cy - 2, cz - 2),
        world(cx + 2, cy + 3, cz + 2),
        FillOperation.KEEP)
def vygeneruj_strom(sirka_kmene: number, start_x: number, start_y: number, start_z: number):
    global zasobnik_x, zasobnik_y, zasobnik_z, zasobnik_delka, zasobnik_sklon, zasobnik_natoceni, zasobnik_hloubka, zasobnik_tloustka, idx
    player.say("Generuji strom (sirka: " + str(sirka_kmene) + ") na [" + str(start_x) + ", " + str(start_y) + ", " + str(start_z) + "]...")
    zasobnik_x = [start_x]
    zasobnik_y = [start_y]
    zasobnik_z = [start_z]
    zasobnik_delka = [14]
    zasobnik_sklon = [randint(0, 4)]
    zasobnik_natoceni = [randint(0, 360)]
    zasobnik_hloubka = [4]
    zasobnik_tloustka = [sirka_kmene]
    while idx < len(zasobnik_x):
        x2 = zasobnik_x[idx]
        y2 = zasobnik_y[idx]
        z2 = zasobnik_z[idx]
        delka = zasobnik_delka[idx]
        sklon = zasobnik_sklon[idx]
        natoceni = zasobnik_natoceni[idx]
        hloubka = zasobnik_hloubka[idx]
        tloustka2 = zasobnik_tloustka[idx]
        idx += 1
        rad_sklon = sklon * Math.PI / 180
        rad_natoceni = natoceni * Math.PI / 180
        dx = Math.sin(rad_sklon) * Math.cos(rad_natoceni)
        dy = Math.cos(rad_sklon)
        dz = Math.sin(rad_sklon) * Math.sin(rad_natoceni)
        kroky = Math.round(delka)
        koncove_x = x2
        koncove_y = y2
        koncove_z = z2
        i = 0
        while i <= kroky + 1 - 1:
            bx2 = Math.round(x2 + dx * i)
            by2 = Math.round(y2 + dy * i)
            bz2 = Math.round(z2 + dz * i)
            # Kořenový náběh u země pro hlavní kmen
            aktualni_tloustka = tloustka2
            if hloubka == 4 and i <= 2:
                aktualni_tloustka = tloustka2 + (3 - i)
            vykresli_prurez(bx2, by2, bz2, aktualni_tloustka)
            koncove_x = bx2
            koncove_y = by2
            koncove_z = bz2
            i += 1
        if hloubka <= 0:
            postav_listi(koncove_x, koncove_y, koncove_z)
        else:
            if hloubka == 4:
                pocet_vetvi = 4
            elif hloubka == 3:
                pocet_vetvi = randint(2, 3)
            else:
                pocet_vetvi = 2
            zakladni_rotace = randint(0, 360)
            v = 0
            while v <= pocet_vetvi - 1:
                nova_delka = delka * (randint(76, 83) / 100)
                nova_tloustka = max(1, tloustka2 * 0.74)
                if hloubka == 4:
                    novy_sklon = randint(36, 48)
                else:
                    novy_sklon = min(64, max(24, sklon + randint(-6, 16)))
                nove_natoceni = zakladni_rotace + v * (360 / pocet_vetvi) + randint(-22, 22)
                zasobnik_x.append(koncove_x)
                zasobnik_y.append(koncove_y)
                zasobnik_z.append(koncove_z)
                zasobnik_delka.append(nova_delka)
                zasobnik_sklon.append(novy_sklon)
                zasobnik_natoceni.append(nove_natoceni)
                zasobnik_hloubka.append(hloubka - 1)
                zasobnik_tloustka.append(nova_tloustka)
                v += 1
    player.say("Hotovo!")