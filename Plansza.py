
from Statek import *
from random import randint, shuffle

class Plansza():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.plansza = [[None for x in range(x)] for i in range(y)]
        self.statki = []
        self.mozliweStrzaly = []
        self.pewneStrzaly = []

    def getPlansza(self):
        return self.plansza

    def tworzenieStatkow(self):
        statek1 = Statek(3, [[0,2], [0,3],[0,4]])
        statek2 = Statek(2, [[4,0],[3,0]])
        statek3 = Statek(1, [[1,0]])
        self.statki.append(statek1)
        self.statki.append(statek2)
        self.statki.append(statek3)


    def generowanieMozliwychStrzalow(self):
        for x in range(0, self.x):
            for y in range(0, self.y):
                self.mozliweStrzaly.append([x, y])
        shuffle(self.mozliweStrzaly)

    def dodajStatkiNaPlansze(self):
        for statek in (self.statki):
            for pozycjaMasztu in (statek.pozycjeMasztow):
                self.getPlansza()[pozycjaMasztu[1]][pozycjaMasztu[0]] = statek

    #def pokazStatki(self):  # pokazuje plansze ze statkami niezatopionymi
    #    for wiersz in (self.getPlansza()):
    #        print("\n")
    #        for statek in (wiersz):
    #            if (statek == None):
    #                print("  *  ", end="")
    #            else:
    #                print("  X  ", end="")
    #    return " "

    def pokazStatki(self):  # pokazuje plansze do gry (maszty tylko zatopione)
        for wiersz in (self.getPlansza()):
            print("\n")
            for statek in (wiersz):
                if (statek == "trafiony"):
                    print("  X  ", end="")
                else:
                    print("  *  ", end="")
        return " "

    def strzel(self, x, y):
        if (plansza.getPlansza()[y][x] == None):
            print("Pudło!")
        elif( plansza.getPlansza()[y][x] == "trafiony"):
            print("Już zatopiony !")
        else:
            print("Trafiłeś w maszt !")
            (plansza.getPlansza())[y][x].pozycjeMasztow.remove([x,y])
            plansza.getPlansza()[y][x].zatopienieMasztu()
            if( plansza.getPlansza()[y][x].czyZatopiony()):
                print("Zatopiłeś cały statek !")
            plansza.getPlansza()[y][x] = "trafiony"

    def oddanieLosowegoStrzalu(self):
        wspolrzedne = self.mozliweStrzaly.pop()
        self.strzel(wspolrzedne[0], wspolrzedne[1])


    def sprawdzCzyTuStrzelales(self, wspolrzedne):
        if(wspolrzedne in self.mozliweStrzaly):
            return False
        return True


    def oddanieStrzaluPoTrafieniu(self, x, y):
        if(x < 0 or x > self.x-1 or y < 0 or y > self.y-1):     #jesli strzal jest poza plansze zwraca pusta liste
            return []

        tymczasowePozycje = []
        tymczasowePozycje.append([x+1, y])
        tymczasowePozycje.append([x, y+1])
        tymczasowePozycje.append([x-1, y])
        tymczasowePozycje.append([x, y-1])

        self.pewneStrzaly.append([x+1, y])
        self.pewneStrzaly.append([x, y+1])
        self.pewneStrzaly.append([x-1, y])
        self.pewneStrzaly.append([x, y-1])

        for poz in (tymczasowePozycje):    # sprawdzanie pozycji do strzalu jesli jest poza plansza: usun.
            if(poz[1] < 0 or poz[1] > self.y-1 or poz[0] < 0 or poz[0] > self.x-1):
                self.pewneStrzaly.remove(poz)
        list(set(self.pewneStrzaly))    #usuwanie duplikatów listy "pewneStrzaly"


    def czyWszystkieStatkiZatopione(self):
        suma = 0
        for statek in (self.statki):
            suma += statek.rozmiarStatku
        if(suma > 0 ):
            return False
        return True

    def pobierzWspolrzedneOdGracza(self):
        wspolrzedne = input("podaj wspolrzedne (ex.: a,b):  ")
        pustyZnak = wspolrzedne.index(" ")
        lista = [(wspolrzedne[0:pustyZnak]),(wspolrzedne[pustyZnak+1::])]
        return lista









plansza = Plansza(5,5)
plansza.tworzenieStatkow()
plansza.dodajStatkiNaPlansze()
#plansza.oddanieStrzaluPoTrafieniu(5,4)
#plansza.strzel(1,0)
#plansza.strzel(3,0)
#plansza.strzel(4,0)
#print(plansza.pewneStrzaly)
#plansza.generowanieMozliwychStrzalow()
print(plansza.pobierzWspolrzedneOdGracza())
#print(plansza.czyWszystkieStatkiZatopione())
#plansza.oddanieLosowegoStrzalu()

