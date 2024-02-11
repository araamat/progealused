#Kirjuta programm, mis küsib kasutajalt sisendina stringi (tekst).
word = input("Kirjuta oma lemmikriik:")
#Eemalda selle sisendi algusest ja lõpust tühikud.
word = word.strip()
print(word)
#String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja et sümbolite arv on paarituarvuline.
lenght = len(word)
if lenght >= 7 and lenght % 2 == 1: # %2 paarituarvuline %-tagastab jäägi.
    print(lenght // 2)
    middle = lenght // 2
    print(word[middle-1: middle+2]) #pythoni puhul tuleb lõpust võtma järgmine, kuna lõpp ei kuulu hulka.
#Väljasta selle stringi kolm keskmist sümbolit.
    
else: 
    print("Ei vasta tingimusele!")
#(stringi meetodid, list)
    
#  //  täidab jagamise tehet kahe arvu vahel, kuid tagastab alati täisarvu tulemuse, 
# ümardatuna nulli poole. See tähendab, et tulemus ei ole ujukomaarv, vaid täisarv, isegi kui jagamise tulemus oleks ujukomaarv.
