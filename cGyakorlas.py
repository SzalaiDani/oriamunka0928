def beolvas():
    szam = int(input("Adja meg a számot: "))
    return szam

def harom():
    for i in range(21):
        print(i, end=" ")

def negy():
    for i in range(20, 57, 2):
        print(i, end=" ")

def otos():
    for i in range(77, -77, -4):
        print(i, end=" ")

def hatos():

    szam1 = beolvas()
    szam2 = beolvas()

    if szam2 < szam1:
        atmenet = szam1
        szam1 = szam2
        szam2 = atmenet

        for i in range(szam1, szam2+1, 1):
            print(i, end=" ")

def hetes():
    szam1 = beolvas()
    szam2 = beolvas()

    szorzat = szam1 * szam2

    if szorzat < 0:
        for i in range(0, szorzat-1, -1):
            print(i, end=" ")
    else:
        for i in range(0, szorzat+1, 1):
            print(i, end=" ")

def nyolcas():
