"""
Funkcja przycinająca listę na podstawie podanego war początkowego i końcowego
wykożystać lambda
"""

def przytnij (wej, start, stop):
    wyj = list()
    for iter in wej:
        if start(iter) :
            wyj.append(iter)
        if stop(iter):
            break
    return wyj

y = przytnij([1,2,3,4,5,6,7,8,9],start = lambda a: a>4, stop= lambda b : b>=7)
print(y)

def test_przytnij():
    assert przytnij([1,2,3,4,5,6,7,8,9],start = lambda a: a>4, stop= lambda b : b==7) == [5, 6, 7]

"""
inne wykorzystanie funjkcji lambda
wygenerwoać funkcję która pobierze jakąś wartość i sprawdzi zadany przez usera warunek - nie che mi się ;p
"""


