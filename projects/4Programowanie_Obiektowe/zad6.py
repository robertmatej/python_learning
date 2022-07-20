"""
Klaas Vector dostarczająca funkcjonalność wektora swobodnego na dwuwymiarowej płaszczyźnie
wektory powinny mieć możlowość dodawaa, odejmownia, monożenia (przez Liczbę),
porównywania po długości, oraz powinny posiadać czytelną reprezentację napisową
"""
from math import sqrt


class Vector:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, kolejna):
        return Vector(self.x + kolejna.x, self.y + kolejna.y)

    def __sub__(self, kolejna):
        return Vector(self.x - kolejna.x, self.y - kolejna.y)

    def __mul__(self, liczba):
        return Vector(self.x * liczba, self.y * liczba)

    def __eq__(self, kolejna):
        return self.x == kolejna.x and self.y == kolejna.y

    def __lt__(self, kolejna):
        return self.length() < kolejna.length()

    def length(self):
        return (self.x **2 + self.y**2)**0.5


def test_dodaj_wektory():
    v1 = Vector(1,2)
    v2 = Vector(2,4)
    wynik = v1 + v2
    a = 2
    b = 3
    assert a + b == 5
    assert wynik.x == 3
    assert wynik.y == 6

def test_odejmij_wektory():
    v1 = Vector(1,2)
    v2 = Vector(2,4)
    wynik = v1 - v2
    assert wynik.x == -1
    assert wynik.y == -2

def test_mnoz_wektor():
    v2 = Vector(2,4)
    wynik = v2 * 3
    a = 2
    b = 3
    assert a * b == 6
    assert wynik.x == 6
    assert wynik.y == 12


def test_rowne():
    v1 = Vector(1, 2)
    v2 = Vector(2, 7)
    v3 = Vector(2, 7)
    assert not (v1 == v2)
    assert v2 == v3

def test_dlugosc_wektora():
    v1 = Vector(2,8)
    assert v1.length() == (2**2 + 8**2)**0.5

def test_wektor_krotszy_niz():
    v1 = Vector(2,4)
    v2 = Vector (2,10)
    assert v1 < v2
    assert not v1 > v2
    