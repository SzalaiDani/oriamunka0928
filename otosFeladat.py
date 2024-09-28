def otos():
    # 5. feladat – HónapNév
    # A program  olvasson be a konzolról egy egész számot! Ha a szám 1 és 12 közötti, akkor legyen a beolvasott szám egy hónap sorszáma! A program írja ki a konzolra a sorszámmal megadott hónap nevét! Hiba esetén legyen hibaüzenet!

    # szám bekérése
    szam = int(input("Kérem adjon meg egy egész számot: "))

    # feltétel létrehozása, kiiratás
    if (szam >= 1 and szam <= 12):
        if szam == 1:
            print("1.hónap - Január")
        elif szam == 2:
            print("2.hónap - Február")
        elif szam == 3:
            print("3.hónap - Március")
        elif szam == 4:
            print("4.hónap - Április")
        elif szam == 5:
            print("5.hónap - Május")
        elif szam == 6:
            print("6.hónap - Június")
        elif szam == 7:
            print("7.hónap - Július")
        elif szam == 8:
            print("8.hónap - Augusztus")
        elif szam == 9:
            print("9.hónap - Szeptember")
        elif szam == 10:
            print("10.hónap - Október")
        elif szam == 11:
            print("11.hónap - November")
        elif szam == 12:
            print("12.hónap - December")
    else:
        print("Nincs "+str(szam)+". hónap!")
