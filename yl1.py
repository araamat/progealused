# yl1
# Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa eurodesse 
# ja väljastab ümardatud tulemuse.(round)

eek = float(input("Sisesta kroonid: ")) #float teeb "ujuvkomaarvuks" ehk 5.0 ja input annab võimaluse kasutajal sisendit anda.
eur = round(eek / 15.6466, 2) #round käsklus ümardab ehk kaks tähendab seal kaks kohta peale koma.
print(eur)

