import math
# from math import pow, pi
def tizenharom():
    # 13. feladat – Kör
    # A program olvassa be a konzolról egy kör sugarát! Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kör sugara nem pozitív!"; egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!

    szam = float(input("Kérem adja meg a kör sugarát: "))

    if (szam >= 0):
        # került
        kerulet = 2 * szam * 3.14
        print("A kör kerülte: "+str(kerulet)+" cm.")
        # terület
        terulet = (szam**2) * 3.14
        print("A kör területe: "+str(terulet)+" négyzetméter.")
    else:
        print("Hiba: a kör sugara nem pozitív!")

    """
    # oraimegoldás:
    r = float(input("Kérem adja meg a kör sugarát: "))

    if r > 0:
        terulet = r**2 * math.pi
        terulet2 = r * r * math.pi
        terulet3 = math.pow(r, 2) * math.pi
        terulet4 = pow(r, 2) * math.pi
        kerulet = 2 * r* math.pi

        print ("A kör területe: "+str(terlet)+", a kör kerülete: "+str(terulet)".")
    else:
        print("Hiba: a kör sugara nem pozitív!")
    """


