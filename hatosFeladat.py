def hatos():
    # 6. feladat – Szögtípus
    # A program  kérjen be a konzolról egy valós számot! Ha ez a szám 0 és 360 közé esik, akkor legyen egy szög mértéke (pl. 60 fok), egyébként a program adjon hibaüzenetet! Ha lehet, a program írja ki a szög mértéke alapján a szög típusát (pl.: 60 -> hegyesszög)!

    szam = float(input("Kérem adjon meg egy valós számot: "))

    if (szam >= 0 and szam <= 360):
        if (szam >= 0 and szam <= 89):
            print(str(szam)+" - a válaszott szögtípus a(z) Hegyesszög!")
        elif (szam == 90):
            print(str(szam)+" - a válaszott szögtípus a(z) Derékszög!")
        elif (szam >= 91 and szam <= 179):
            print(str(szam)+" - a válaszott szögtípus a(z) Hegyesszög!")
        elif (szam == 180):
            print(str(szam)+" - a válaszott szögtípus a(z) Egyenesszög!")
        elif (szam >= 181 and szam <= 360):
            print(str(szam)+" - a válaszott szögtípus a(z) Homorúszög!")
    else:
        print("Nem létezik ilyen szög!")