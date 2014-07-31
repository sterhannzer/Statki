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
        self.ostatnioTrafionyStatek = None
        self.dodatkowyRuchZaTrafienie = True

    def getPlansza(self):
        return self.plansza

    def tworzenieStatkow(self):
        statek1 = Statek(3, [[0, 2], [0, 3], [0, 4]])
        statek2 = Statek(2, [[4, 0], [3, 0]])
        statek3 = Statek(1, [[1, 0]])
        self.statki.append(statek1)
        self.statki.append(statek2)
        self.statki.append(statek3)

    def dodajStatkiNaPlansze(self):
        for statek in (self.statki):
            for pozycjaMasztu in (statek.pozycjeMasztow):
                self.getPlansza()[pozycjaMasztu[1]][pozycjaMasztu[0]] = statek

    def drukowanieLiczbPoziom(self):
        for liczba in range(1, self.x+1):
            print(liczba, end="")
            print(4*" ", end="")

    def drukowaniePlanszy(self, planszaGracza, planszaKomputera):
        print("   Twoja plansza:" + (self.x*5+3-17)*" "+11*" "+"Plansza komputera:")
        str(print("   ", end="")) + str(self.drukowanieLiczbPoziom()) + str(print(11*" ", end="")) + str(self.drukowanieLiczbPoziom()) + str(print("\n"))
        for wiersz in range(len(planszaGracza.getPlansza())):
            str(print(wiersz+1, end="")) + str(self.pokazStatki(planszaGracza, wiersz)) + str(print("          ", end="")) + str(print(wiersz+1, end="")) + str(self.pokazStatki(planszaKomputera, wiersz)) + str(print("\n"))

    def pokazStatki(self, plansza, wiersz):  # pokazuje plansze do gry (maszty tylko zatopione)
        for statek in (plansza.getPlansza()[wiersz]):

            if (statek == "trafiony"):
                print("  X  ", end="")
            elif(statek == "pudlo"):
                print("  O  ", end="")
            else:
                print("  *  ", end="")

    def strzel(self, x, y):
        if (self.getPlansza()[y][x] is None):
            print("Pudło!", (x+1, y+1))
            self.getPlansza()[y][x] = "pudlo"
        elif(self.getPlansza()[y][x] == "trafiony"):
            print("Już zatopiony !", (x+1, y+1))
        elif(self.getPlansza()[y][x] == "pudlo"):
            print("już tu strzelałeś !", (x+1, y+1))
        else:
            print("Trafiłeś w maszt !", (x+1, y+1))
            (self.getPlansza())[y][x].pozycjeMasztow.remove([x, y])
            self.getPlansza()[y][x].zatopienieMasztu()
            if(self.getPlansza()[y][x].czyZatopiony()):
                print("Zatopiłeś cały statek !" + "\n")
            self.getPlansza()[y][x] = "trafiony"

    def generowanieMozliwychStrzalow(self):
        for x in range(0, self.x):
            for y in range(0, self.y):
                self.mozliweStrzaly.append([x, y])
        shuffle(self.mozliweStrzaly)

    def oddanieLosowegoStrzalu(self):
        wspolrzedne = self.mozliweStrzaly.pop()
        self.strzel(wspolrzedne[0], wspolrzedne[1])

    def sprawdzCzyTuStrzelales(self, wspolrzedne):
        if(wspolrzedne in self.mozliweStrzaly):
            return False
        return True

    def generowaniePewnychStrzalowPoTrafieniu(self, x, y):
        if(x < 0 or x > self.x-1 or y < 0 or y > self.y-1):  # jesli strzal jest poza plansze zwraca pusta liste
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

        for poz in (tymczasowePozycje):  # sprawdzanie pozycji do strzalu jesli jest poza plansza: usun.
            if(poz[1] < 0 or poz[1] > self.y-1 or poz[0] < 0 or poz[0] > self.x-1):
                self.pewneStrzaly.remove(poz)
        tymczasowePewneStrzaly = []
        [tymczasowePewneStrzaly.append(x) for x in self.pewneStrzaly if x not in tymczasowePewneStrzaly and x in self.mozliweStrzaly]  # usuwanie duplikatów w tymczasowychstrzalach
        self.pewneStrzaly = tymczasowePewneStrzaly

    def strzelajDopokiNieZatopiszCalegoStatku(self):
        while(True):
            if not self.dodatkowyRuchZaTrafienie or len(self.mozliweStrzaly) == 0:
                self.dodatkowyRuchZaTrafienie = True
                break
            if(self.ostatnioTrafionyStatek is None):
                # tutaj może pojawić się problem kiedy lista możliwe strzały jest pusta.
                if(isinstance(self.getPlansza()[self.mozliweStrzaly[-1][1]][self.mozliweStrzaly[-1][0]], Statek)):  # sprawdzanie czy strzał losowy będzie celny
                    self.ostatnioTrafionyStatek = self.getPlansza()[self.mozliweStrzaly[-1][1]][self.mozliweStrzaly[-1][0]]
                    self.generowaniePewnychStrzalowPoTrafieniu(
                        self.mozliweStrzaly[-1][0],
                        self.mozliweStrzaly[-1][1]
                    )
                    self.oddanieLosowegoStrzalu()
                    self.dodatkowyRuchZaTrafienie = True
                    continue
                else:
                    self.oddanieLosowegoStrzalu()
                    break
            else:
                while(True):
                    if(not self.ostatnioTrafionyStatek.czyZatopiony()):  # jesli nie jest zatopiony to:                               #jesli poprzednio był celny strzał to w pewnych strzałach będą
                        wspolrzedne = self.pewneStrzaly.pop()       # pozycje w pierwszej kolejnosci do strzalu.
                        if(wspolrzedne in self.mozliweStrzaly):
                            self.mozliweStrzaly.remove(wspolrzedne)
                        if(isinstance(self.getPlansza()[wspolrzedne[1]][wspolrzedne[0]], Statek)):
                            self.strzel(wspolrzedne[0], wspolrzedne[1])
                            # tutaj trzeba sprawdzac czy ten statek nie jest przypadiem juz zatopiony jesli tak to wtedy nadac OSTATIONTRAFIONYSTATEK = none
                            if(self.ostatnioTrafionyStatek.czyZatopiony()):
                                self.ostatnioTrafionyStatek = None
                                self.usunStrzalyDookolaZatopionegoStatku()
                                break
                            else:
                                self.generowaniePewnychStrzalowPoTrafieniu(wspolrzedne[0], wspolrzedne[1])
                                continue
                        else:
                            self.strzel(wspolrzedne[0], wspolrzedne[1])
                            self.dodatkowyRuchZaTrafienie = False
                            break
                    else:
                        self.usunStrzalyDookolaZatopionegoStatku()
                        self.ostatnioTrafionyStatek = None
                        self.dodatkowyRuchZaTrafienie = True
                        break

    def usunStrzalyDookolaZatopionegoStatku(self):
        for strzal in self.pewneStrzaly:
            self.mozliweStrzaly.remove(strzal)

    def czyWszystkieStatkiZatopione(self):
        suma = 0
        for statek in (self.statki):
            suma += statek.rozmiarStatku
        if(suma > 0):
            return False
        return True

    def pobierzWspolrzedneOdGracza(self):
        wspolrzedne = input("podaj wspolrzedne (ex.: x y):  ")
        pustyZnak = wspolrzedne.index(" ")
        lista = [int((wspolrzedne[0:pustyZnak])), int((wspolrzedne[pustyZnak+1::]))]
        return lista

    def przeniesStrzalyZPewnych(self):
        for strzal in self.pewneStrzaly:
            self.mozliweStrzaly.append(strzal)
        self.pewneStrzaly = []
