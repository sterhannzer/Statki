
class Statek():
    def __init__(self, rozmiarStatku, pozycjeMasztow):   #pozycjeMasztow jest listą np. [[1,2],[2,2]]
        self.rozmiarStatku = rozmiarStatku
        self.pozycjeMasztow = pozycjeMasztow
        self.zatopiony = False

    def czyZatopiony(self):
        return self.zatopiony

    def getPozycjeMasztow(self):
        return self.pozycjeMasztow

    def zatopienieMasztu(self):
        self.rozmiarStatku -= 1
        if(self.rozmiarStatku == 0):
            self.zatopiony = True

    def getRozmiarStatku(self):
        return self.rozmiarStatku



