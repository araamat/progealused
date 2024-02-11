# yl2
# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)

from math import pi # impordib ainult pi moodulist math ning seda saab seejärel kasutada otse ilma mooduli nime ees eesliitega.
radius = float (input("Sisesta raadius: "))
area = pi * radius ** 2
perimeter = 2 * pi *radius
area2 = round(area, 3) #lõin ümardamise vahele nagu yl1.
perimeter2 = round(perimeter, 3)
print("Pindala:", area2, "Ümbermõõt", perimeter2)
