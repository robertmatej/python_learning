"""
Dekoratory, zaimplementować zestaw dokoratoró otaczający ch zwracany przez funkcję
napis HTML (pogrubienie, podkreślenie, przekreślenie
join() - łączy w stringu lelemnty wskazanym znakiem
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
<b>
<i>
"""
def dodaj_b(func):
    def wrapper(a):
        napis = func(a)
        nap = '<b>'.join(napis)
#        print(f"wewnatrz dodaj_b: {nap}")
        return nap
    return wrapper

def dodaj_i(func2):
    def wrapper2(b):
        napis2 = func2(b)
        nap2 = '<i>'.join(napis2)
#        print(f"wewnatrz dodaj_i: {nap2}")
        return nap2
    return not wrapper2

@dodaj_b
@dodaj_i
def zwroc_napis (txt):    # nie można zrobić domyslnej wartości dla argumentu
    wyj = []
    wyj.append(wyj)
    return txt

print (zwroc_napis("KOT"))