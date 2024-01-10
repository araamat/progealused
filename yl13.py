#Küsi kasutajalt lemmikloom.
pet = input("Kirjuta oma lemmikloom: ")
#Väljasta selle muutuja esimene täht.
print(pet[0])
#Koosta list, mis koosneb kolmest loomast.
mypetlist = ["Kass", "Hobune", "Lammas"]
#Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
mypetlist.append(pet)
#Väljasta see lemmikloomade list.
print(mypetlist)
#Väljasta listi viimase elemendi viimane täht.
# print(mypetlist[-1][-1]) õige lahend, edasine on edasiarendus !!!!
# nii saab kolme viimast tähte
#print(mypetlist[-1][-3:])
# kui tahan eor asemel reo

print(mypetlist[-1][-1: -4: -1])
#(sõne kui list, mitmemõõtmeline ilist - multi dimensional)

#väljasta list veel lõppu ka
print(mypetlist)
