# Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi (ära kasuta min funktsiooni). (muutuja - variable, tingimus - condition, if-lause - if statement)
# 1. Küsi kasutajalt arv 1
# 2. Küsi kasutajalt arv 2
# 3. Leia miinimum väärtus
# 4. Väljasta see

a = int(input("Sisesta arv a: "))
b = int(input("Sisesta arv b: "))
if b > a:
    print ("miinimum on", a)
else:  
    print ("miinimum on", b)