# yl1
# Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa eurodesse 
# ja väljastab ümardatud tulemuse.(round)

eek = float(input("Sisesta kroonid: "))
eur = round(eek / 15.6466, 2)
print(eur)

