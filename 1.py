from abc import ABC, abstractmethod

class Ciasto(ABC):
    @abstractmethod
    def przygotuj(self):
        pass
    
    @abstractmethod
    def sprawdz(self):
        pass
    
    @abstractmethod
    def piecz(self, czas, temperatura):
        pass
    
    @abstractmethod
    def ocen(self):
        pass

class Ciastko(Ciasto):
    def __init__(self, maka, cukier, woda):
        self.maka = maka
        self.cukier = cukier
        self.woda = woda

class Szarlotka(Ciasto):
    def __init__(self):
        self._czy_upieczone = False
        self._licznik_sprawdzen = 0
        self.__cynamon = False

    def przygotuj(self):
        self._czy_upieczone = False
        self._licznik_sprawdzen = 0
        self.__cynamon = False

    def sprawdz(self):
        if self._licznik_sprawdzen < 3:
            return False
        else:
            return True

    def piecz(self, czas, temperatura):
        if czas >= 55 and czas <= 60 and temperatura >= 180 and temperatura <= 200:
            if self.__cynamon:
                while not self._czy_upieczone:
                    if self.sprawdz():
                        self._czy_upieczone = True
                    else:
                        self._licznik_sprawdzen += 1
            else:
                print("Nie dodano cynamonu. Szarlotka nie bedzie pieczona.")
        else:
            print("Nieodpowiednie parametry czasu i/lub temperatury.")

    def ocen(self):
        return self._czy_upieczone

    def cynamon(self):
        self.__cynamon = True

class Sernik(Ciasto):
    def __init__(self):
        self._czy_upieczone = False
        self._licznik_sprawdzen = 0
        self.__rodzynki = 0

    def przygotuj(self):
        self._czy_upieczone = False
        self._licznik_sprawdzen = 0
        self.__rodzynki = 0

    def sprawdz(self):
        if self._licznik_sprawdzen < 3:
            return False
        else:
            return True

    def piecz(self, czas, temperatura):
        if czas >= 65 and czas <= 75 and temperatura >= 200 and temperatura <= 220:
            if self.__rodzynki >= 30:
                while not self._czy_upieczone:
                    if self.sprawdz():
                        self._czy_upieczone = True
                    else:
                        self._licznik_sprawdzen += 1
            else:
                print("Za malo rodzynkow. Sernik nie bedzie pieczony.")
        else:
            print("Nieodpowiednie parametry czasu i/lub temperatury.")

    def ocen(self):
        return self._czy_upieczone

    def rodzynki(self, liczba=10):
        self.__rodzynki += liczba


szarlotka = Szarlotka()
szarlotka.przygotuj()
szarlotka.cynamon()
szarlotka.piecz(60, 190)
print("Szarlotka upieczona:", szarlotka.ocen())

sernik = Sernik()
sernik.przygotuj()
sernik.rodzynki(30)
sernik.piecz(70, 200)
print("Sernik upieczony:", sernik.ocen())
