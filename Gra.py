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
            print("\nTy :", wspolrzedne)
            planszaKomputera.strzel(wspolrzedne[0]-1,wspolrzedne[1]-1)
            if planszaKomputera.getPlansza()[wspolrzedne[1]-1][wspolrzedne[0]-1] == "trafiony":
                if planszaKomputera.czyWszystkieStatkiZatopione():
                    break
                planszaGracza.drukowaniePlanszy(planszaGracza, planszaKomputera)
                print ("----------------------------------------------------------------------------------------")
                continue
            else:
                print("\nKomputer :")
                planszaGracza.strzelajDopokiNieZatopiszCalegoStatku()
                if planszaGracza.czyWszystkieStatkiZatopione():
                    break
                print("\n")
            planszaGracza.drukowaniePlanszy(planszaGracza, planszaKomputera)
            print ("----------------------------------------------------------------------------------------")
            break
        except IndexError:
            print("Strzeliłeś poza plansze ! Spróbuj jeszcze raz :)")
            continue

