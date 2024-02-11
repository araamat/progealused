# Arvu arvamise mäng. 
# Arvuti mõtleb välja arvu nullist sajani. 
# Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. 
# Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. 
# Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)

import random

# Arvuti valib juhusliku arvu vahemikus 0 kuni 100
salajane_arv = random.randint(0, 100)

# Mängu loogika
kasutaja_pakkumine = None
katsete_arv = 0

while kasutaja_pakkumine != salajane_arv:
    kasutaja_pakkumine = int(input("Paku arv 0-st 100-ni: "))
    katsete_arv += 1

    if kasutaja_pakkumine < salajane_arv:
        print("Pakkumine on liiga väike. Proovi uuesti.")
    elif kasutaja_pakkumine > salajane_arv:
        print("Pakkumine on liiga suur. Proovi uuesti.")
    else:
        print(f"Õige! Arvuti valitud arv oli {salajane_arv}. Sa pakkusid õigesti {katsete_arv} katsega.")

# salajane_arv muutuja määratakse juhuslikule arvule vahemikus 0 kuni 100, kasutades random.randint() funktsiooni.
# kasutaja_pakkumine muutuja algväärtus on None, mis tähendab, et kasutajalt pole veel sisendit saadud.
# katsete_arv muutuja hoiab meeles, mitu korda kasutaja on pakkunud.
# while tsükkel töötab seni, kuni kasutaja pakkumine ei ole võrdne salajase arvuga.
# Iga tsükli iteratsiooni käigus küsitakse kasutajalt pakkumist ning kontrollitakse, kas see on suurem või väiksem kui salajane arv.
# Kui kasutaja pakkumine on väiksem, väljastatakse vastav teade.
# Kui kasutaja pakkumine on suurem, väljastatakse vastav teade.
# Kui kasutaja pakkumine on õige, väljastatakse vastav teade ning mäng lõpetatakse.
# katsete_arv hoiab meeles, mitu korda kasutaja on pakkunud, ning see väljastatakse lõppseisundis, kui kasutaja on arvu ära arvanud.
