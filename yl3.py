# yl3
# Kirjuta programm, mis küsib kasutajalt täisarvu n vahemikus 1-9. 
# Arvuta n + nn + nnn väärtus ja väljasta see. 
# (Näiteks kui kasutaja sisestab 2, siis on vaja väljastada tulemus 2 + 22 + 222 = 246). 
# Ära kasuta korrutamistehet. Ülesanne on lahendatav ainult liitmise operaatorit kasutades.

n = input("Sisesta täisarv vahemikus 1-9: ")
nn = n + n
nnn = n + n + n
total = int(n) + int(nn) + int(nnn)   #
print(n + " + " + nn, "+", nnn, "=", total)

#INT  on Pythoni andmetüüp ja funktsioon, mis teisendab argumendiks antud väärtuse täisarvuks... 
# ...Kui antud väärtus on arvuline string või ujukomaarv, teisendatakse see täisarvuks, kaotades ujukohad, kui need eksisteerivad.

# küsime kasutajalt täisarvu n
# leiame nn
# leiame nnn
# leiame n+nn+nnn
# väljastame
