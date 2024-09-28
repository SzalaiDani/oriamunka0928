def tizenot():
    # 15. feladat – Téglalap1
    # A program olvasson be a konzolról két valós számot! Ha mindkét szám pozitív, akkor legyenek a beolvasott számok egy téglalap oldalai. A program számítsa ki a téglalap kerületét, területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"!

    szam1 = float(input("Kérem adjon meg egy valós számot: "))
    szam2 = float(input("Kérem adjon meg még egy valós számot: "))

    if (szam1 >= 0 and szam2 >= 0):
        # kerület
        kerulet = 2 * (szam1 + szam2)
        print("A téglalap kerülete: "+str(kerulet))
        # terület
        terulet = szam1 * szam2
        print("A téglalap területe: " + str(terulet))
    else:
        print("Hiba: a téglalap oldalai nem pozitívak!")
