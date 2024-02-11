#Väljasta korduslause abil 8 korrutis arvudega 0..12 ja vorminda väljund nii:
# 8 x 0 = 0
# 	8 x 1 = 8
# 	8 x 2 = 16
# 	…
# 	8 x 12 = 96
# Täienda programmi nii, et kasutajalt küsitakse arv x, mille kohta korrutustabel väljastatakse

b = ""
while not b.isnumeric():
    b = input("Sisesta number: ")

b = int(b)

for a in range(0, 13):
    print(b, "x", a, "=", a * b)

# Muutuja b algväärtuseks määratakse tühi string "".
# Seejärel käivitatakse while tsükkel, mis töötab seni, kuni kasutaja sisestatud string ei ole arvuline (kasutades isnumeric() meetodit).
# Kui kasutaja sisend ei ole arvuline, küsitakse kasutajalt uut sisendit, mida kontrollitakse uuesti.
# Kui sisend on arvuline, muudetakse see täisarvuks int() funktsiooniga.
# Seejärel käivitatakse for tsükkel vahemikus 0 kuni 12 (sealhulgas 0 ja 12), mille sees korrutatakse kasutaja 
    #sisestatud arv iga arvuga vahemikus 0 kuni 12 ning tulemus väljastatakse.
