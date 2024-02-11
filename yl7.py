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


#INT  on Pythoni andmetüüp ja funktsioon, mis teisendab argumendiks antud väärtuse täisarvuks... 
# ...Kui antud väärtus on arvuline string või ujukomaarv, teisendatakse see täisarvuks, kaotades ujukohad, kui need eksisteerivad.
    
#ELSE -  "muul juhul". Seda kasutatakse siis, kui soovitakse, et mingi plokk koodi töötaks ainult siis, kui ükski eelnevatest tingimustest pole tõene.