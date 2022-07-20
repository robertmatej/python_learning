"""
funkcja obliczająca koszt przejazdu na podtawie dancy zebranych od usera
odleglość, cena paliwa, spalania, nazwy miast
"""

def koszt_przejazdu(zmienna):
    print (zmienna)
    spalanie = float(zmienna[0])
    cena_pal = float(zmienna[2])
    odleglosc = float(zmienna[1])
    koszt = round((odleglosc/100)*spalanie*cena_pal,2)
    print (f'koszt przejazduu {koszt}')
    return koszt

def pobierz_dane():
    dane_we = ['spalanie','odleglość','cena paliwa']
    dane_wy = []
    for i in dane_we:
        dane_wy.append(input(f"podaj {i}: "))
#        print (tuple(dane_wy))
    return dane_wy

koszt_przejazdu(pobierz_dane())
