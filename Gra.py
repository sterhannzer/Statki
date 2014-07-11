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
        print("Przegrałeś z komputerem :(")
        break
    elif(planszaKomputera.czyWszystkieStatkiZatopione()):
        print("Gratulacje !!!  Wygrałeś z komputerem !")
        break
    while(True):
        wspolrzedne = plansza.pobierzWspolrzedneOdGracza()
        try:
            planszaKomputera.strzel(wspolrzedne[0],wspolrzedne[1])
            break
        except IndexError:
            print("Strzeliłeś poza plansze! Spróboj jeszcze raz")
            continue
    planszaKomputera.pokazStatki()

