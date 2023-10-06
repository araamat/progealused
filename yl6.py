# Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni). (loogikatehted - logic operators)

# Küsi kasutaja 1 arv
# Küsi kasutaja 2 arv
# Küsi kasutaja 3 arv
# Leia maksimum arv
# Väljastamine

a = int(input("Sisesta arv a: "))
b = int(input("Sisesta arv b: "))
c = int(input("Sisesta arv c: "))

if a > b and a > c:
    print("maksimum on", a)

elif b > c:
    print("maksimum on", b)

else:
    print("maksimum on", c)
    