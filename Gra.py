from Plansza import *
from Statek import *

planszaGracza = Plansza(6,6)
planszaGracza.tworzenieStatkow()
planszaGracza.dodajStatkiNaPlansze()
planszaGracza.generowanieMozliwychStrzalow()

planszaKomputera = Plansza(6,6)
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
            print("\nTy :")
            planszaKomputera.strzel(wspolrzedne[0],wspolrzedne[1])
            if planszaKomputera.getPlansza()[wspolrzedne[1]][wspolrzedne[0]] == "trafiony" and not planszaKomputera.czyWszystkieStatkiZatopione():
                continue
            else:
                print("\nKomputer :")
                planszaGracza.strzelajDopokiNieZatopiszCalegoStatku()
                print("\n")
            planszaGracza.drukowaniePlanszy(planszaGracza, planszaKomputera)

        except IndexError:
            print("Strzeliłeś poza plansze! Spróboj jeszcze raz")
            continue