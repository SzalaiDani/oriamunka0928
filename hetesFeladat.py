import math
def hetes():
    # 7. feladat – Négyzetgyök
    # A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!

    szam = float(input("Kérem adjon meg egy valós számot: "))

    if (szam >= 0):
        szam = math.sqrt(szam)
        print(szam)
    else:
        print("Kérem adjon meg pozitív számot!")