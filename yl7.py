# Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. 
# (paarisarvu mõiste - odd/even)

# Kasutaja sisestab arvu.
# Leia paarisarv.
# Väljastamine.

# jäägiga jagamine: modulo

a = int(input("Sisesta täisarv: "))

if a % 2:
    print(a, "on paaritu arv")

else: 
    print(a, "on paaris arv")
