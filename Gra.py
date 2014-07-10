from Plansza import *
from Statek import *

planszaGracza = Plansza(5,5)
planszaGracza.tworzenieStatkow()
planszaGracza.dodajStatkiNaPlansze()

planszaKomputera = Plansza(5,5)
planszaKomputera.tworzenieStatkow()
planszaKomputera.dodajStatkiNaPlansze()

while (True):
    if(planszaGracza.czyWszystkieStatkiZatopione()):
        print("Gratulacje Wygrałeś z komputerem !")
        break
    elif(planszaKomputera.czyWszystkieStatkiZatopione()):
        print("Przegrałeś z komputerem :( ")
        break
    while(True):
        wspolrzedne = plansza.pobierzWspolrzedneOdGracza()

