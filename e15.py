# függvény
def egeszBeolvas():
    szam = float(input("Kérem adjon meg egy egész számot: "))
    return szam

# eljárás
def teglalap():

    oldal1 = egeszBeolvas()
    oldal2 = egeszBeolvas()

    if (oldal1 > 0 and oldal2 > 0):
        kerulet = round(2 * (oldal1 + oldal2), 2)
        terulet = round(oldal1 * oldal2, 2)

        print("A téglalap kerülte: "+str(kerulet)+", területe: "+str(terulet)+".")
    else:
        print("Hiba: A téglalap oldalai nem pozitívak!")