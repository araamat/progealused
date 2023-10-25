# Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. 
# Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi. 
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. 
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)

# Sisesta kolmnurga küljed.
# Float annab komaarvud.
# Kontrollin A-d.


a= float(input("Sisesta külg a: "))
b= float(input("Sisesta külg b: "))
c= float(input("Sisesta külg c: "))

if a < b + c or b < a + c or c < a + b:
    print("on kolmnurk")
    
else:
    print("ei ole kolmnurk")

print(a, b, c)