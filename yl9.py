# Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. 
# Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi. 
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. 
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)

# Sisesta kolmnurga küljed.
# Float annab komaarvud.
# Kontrollin A-d.

def kolmnurga_liik(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Sellise külgedega kolmnurka ei eksisteeri"
    elif a == b == c:
        return "Võrdkülgne kolmnurk"
    elif a == b or a == c or b == c:
        return "Võrdhaarne kolmnurk"
    else:
        return "Erikülgne kolmnurk"

def main():
    try:
        a = float(input("Sisestage esimese külje pikkus: "))
        b = float(input("Sisestage teise külje pikkus: "))
        c = float(input("Sisestage kolmanda külje pikkus: "))
        
        vastus = kolmnurga_liik(a, b, c)
        print(vastus)
    except ValueError:
        print("Palun sisestage arvulised väärtused külgede pikkusteks.")

if __name__ == "__main__":
    main()

#if __name__ == "__main__": on Pythoni konstruktsioon, mis kontrollib, kas käivitatud skript on peamine programmifail 
    # või seda imporditakse teisest failist. 
#Kui käivitatakse otse, mitte importimise kaudu, siis see tingimus kehtib ja sellega saab tagada, et peamine 
    # programmifunktsioon (tavaliselt nimetatakse seda main-iks) käivitatakse.
#main() funktsiooni kutsumine toimub ainult siis, kui see skript käivitatakse otse, mitte kui seda imporditakse teise skripti.

#ELSE -  "muul juhul". Seda kasutatakse siis, kui soovitakse, et mingi plokk koodi töötaks ainult siis, kui ükski eelnevatest tingimustest pole tõene.

# a= float(input("Sisesta külg a: "))
# b= float(input("Sisesta külg b: "))
# c= float(input("Sisesta külg c: "))

# if a < b + c or b < a + c or c < a + b:
#     print("on kolmnurk")
    
# else:
#     print("ei ole kolmnurk")

# print(a, b, c)