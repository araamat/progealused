#Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv. 

text = "Ametikool"
vowels = "a, e, i, o, u, õ, ä, ö, ü".split(", ")
print (vowels)

count = 0
# c suvaline, hetkel character lühend
for c in text.lower(): #ametikool (lower teeb kõik väiksteks tähtedeks)
    if c in vowels:
        count += 1 #count = count + 1 ehk väärtust kasvatatakse ühe korra

print(count)

