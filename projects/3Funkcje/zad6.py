"""
funkcja spłaszczacjąca zagnieżdzone listy w liście

"""

def splaszcz (wejscie):
    wyjscie = list()
    for element in wejscie:
        if type(element) is list:
            wyjscie.extend(splaszcz(element))            #extend (dodaje element listy lub listę do listy) robi robotę, append (dodaje element do listy) nie dzawało rady
#            print(wyjscie)
        else:
            wyjscie.append(element)

    return wyjscie

print ((f'wersja 1 {splaszcz([1,2,3,[4,[5,6,7,[8]],4,4],5,5,5])}'))
#print (splaszcz([1,2,3,[4,[5,6,7,[8]],4,4],5,5,5]))  # to co wyżej bez napisów wyrazniesze do odczytu

"""
Metoda na generatorach
"""

def splaszcz_gen(input):
#    output = list
    for elem in input:
        if isinstance(elem,list):                   #efek dzialan ia identyczny jak: type(elem) is list
            for inter in splaszcz_gen(elem):
                yield inter                        #nie oblicza od razu, trzyma awrtośc do momentu wywołania
        else:
            yield elem

#print wywołuje yelda w kazdje pętli, list potrzebny zeby wbyciagnąć wartości, a nie dostać adres generatora
print (f"z generatora: {list(splaszcz_gen([1,2,3,[4,[5,6,7,[8]],4,4],5,5,5]))}")
#print (list(splaszcz([1,2,3,[4,[5,6,7,[8]],4,4],5,5,5])))  # to co wyżej bez napisów wyrazniesze do odczytu

def test_splaszcz_gen ():
    assert list(splaszcz_gen((splaszcz([1,2,3,[4,[5,6,7,[8]],4,4],5,5,5])))) == [1, 2, 3, 4, 5, 6, 7, 8, 4, 4, 5, 5, 5]