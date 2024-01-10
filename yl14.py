# Kirjuta programm, mis küsib kasutajalt failinime kujul “failinimi.ext” (ext - extension - faili laiend)
filename = input("Sisesta fail koos failinimega kujul failinimi.ext:")
# ja prindib välja laiendi (“ext”). (str.split)
print("Faili laiendiks on:", filename.split(".")[-1])

#-1 tähistab viimast kohta listis(-2 on eelviimane jne). Kui panna 0,1,2....siis hakkab vasakult-->paremale.
