#AI
# Küsi kasutajalt arv x
x = int(input("Sisestage arv x: "))

# Väljasta korrutustabel x-ga arvudele 0 kuni 12
for i in range(13):
    result = x * i
    print(f"{x} x {i} = {result}")