# Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha, 
# kui elukoht on Saaremaa, siis väljastab mingi kommentaari, küsib kasutajalt vanuse, 
# kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida, 
# kui vanus on 18, siis õnnitleb täisealiseks saamise puhul, kui kasutaja on vanem kui 18, 
# siis ütleb, et kasutaja võib autot juhtida. (sõne - string) 


# 1. Küsime nime
# 2. Tervitame
# 3. Küsime elukohta
# 4. Kontrollime elukohta
# 5. ...kui saarema, siis...
# 6. küsime vanust
# 7. kontrollime
# 8. kui vanus, siis ...

name = input("nimi: ").capitalize() #capitalize teeb suureks esimese tähe, kui kirjutad väikesega
print("Tere,", name + "!")

location = input("Teie elukoht: ").lower() #lower teeb teksti väikesteks tähtedeks
if "saaremaa" in location:
    print("Rööm!")

age = int(input("Teie vanus:"))
if age < 18:
    print("Oled liiga noor, et autot juhtida.")
elif age == 18:
    print("Õnnitlen täisealiseks saamise puhul!")
else:
    print("Võid autot juhtida!")


#lõpp võib nii ka
#if age == 18:
    #print("Õnnitlen täisealiseks saamise puhul!")
#if age > 18:
    #print("Võid autot juhtida!")