"""
zadanie 1.2 przerobione na funkcje
obliczyć pole trapezu
"""

def pole (podst_a = 4, podst_b = 2, wys = 3):
    return 0.5*(podst_a+podst_b)*wys

def test_pole ():
    assert pole() == 9

    