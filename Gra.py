from Plansza import *
from Statek import *

planszaGracza = Plansza(5,5)
planszaGracza.tworzenieStatkow()
planszaGracza.dodajStatkiNaPlansze()
planszaGracza.generowanieMozliwychStrzalow()

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
        wspolrzedne = planszaGracza.pobierzWspolrzedneOdGracza()
        try:
            planszaKomputera.strzel(wspolrzedne[0],wspolrzedne[1])
            if planszaKomputera.getPlansza()[wspolrzedne[1]][wspolrzedne[0]] == "trafiony" and not planszaKomputera.czyWszystkieStatkiZatopione():
                print("Plansza komputera: ")
                planszaKomputera.pokazStatki()
                continue
            else:
                planszaGracza.strzelajDopokiNieZatopiszCalegoStatku()
                planszaGracza.pokazStatki()
                print("\n \n")
        except IndexError:
            print("Strzeliłeś poza plansze! Spróboj jeszcze raz")
            continue

