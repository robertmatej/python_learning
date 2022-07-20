def policz_znaki(napis, znak_poczatek="<", znak_koniec='>'):
    #napis = 'ala ma<kota> a kot ma ale'
  #  znak_poczatek = '<'

    wynik = 0
    poziom_zaglebienia = 0
    for znak in napis:

            if znak == znak_poczatek:

                poziom_zaglebienia +=1
            elif znak == znak_koniec:
                poziom_zaglebienia -= 1
            else:
                wynik+= poziom_zaglebienia

    return wynik


# #testy pomocnicza
# def test_0_poziom_zaglebienia():
#     assert policz_znaki (poziom_zaglebienia)==0
#
# def test_1_poziom_zaglebienia():
#     assert policz_znaki (poziom_zaglebienia)==1
#
# def test_3_poziom_zaglebienia():
#     assert policz_znaki (poziom_zaglebienia)==3
#
# def test_3_poziom_zaglebienia():
#     assert policz_znaki (poziom_zaglebienia)==3


def test_policz_znaki_pusty_napis():
    assert policz_znaki('') == 0


def test_policz_znaki_napis_bez_nawias():
    assert policz_znaki('to jest napis') == 0


def test_policz_znaki_pierwszy_level():
    assert policz_znaki('ala ma<kota> a kot ma ale') == 4


def test_policz_znaki_drugi_level():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', "]") == 18


def test_policz_znaki_trzeci_level():
    assert policz_znaki('a <a<a<a>>>') == 6
