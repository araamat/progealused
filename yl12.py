#yl12 Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see

mylist = ["apple", "strawberry", "rasberry"]
#Väljasta listi esimene väärtus
print(mylist[0])
#Lisa listi lõppu uus puuvili
mylist.append("pear")
print(mylist)
#Väljasta listi viimane väärtus
print(mylist[-1])
#Muuda ühe elemendi väärtust ja väljasta kogu list
mylist[0]= "banana"
print(mylist)
#Kontrolli kas väärtus (näiteks õun) eksisteerib listis
check = "banana"
if check in mylist:
    print(check, "is in list.")
else:
    print(check, "is not in list.")
#Väljasta listi pikkus
print(len(mylist))
#Eemalda listist element ja väljasta kogu list
mylist.remove("rasberry")
print(mylist)
#Muuda listi järjekord vastupidiseks
mylist.reverse()
print(mylist)
#Sorteeri list ja väljasta
mylist.sort() #tähestikuline järjekord sort käsuga
print(mylist)

# (jada, list, listi element, listi meetodid)
# https://www.w3schools.com/python/python_lists.asp