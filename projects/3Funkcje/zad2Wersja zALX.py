def wiecej_niz(napis, prog):
    wynik = set()
    napis = napis.lower()

    for litera in napis.lower():
        litera = litera.lower()
        if napis.count(litera) > prog:
            wynik.add(litera)
    return wynik


def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz('', 0) == set()


def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz('aaaaabbbccd', 2) == {'a', 'b'}


def test_wiecej_niz_dla_niepustego_napisu_duze_male_litery():
    assert wiecej_niz('aaaAAbbbccd', 4) == {'a'}
