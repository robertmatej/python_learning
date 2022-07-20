""""
gra polegajaca na poszukiwaniu skabu na planszy 2d 10x10
user wprowadza konmendy zmieniajace polozenie postaci
po kazdym ruchu info czy zbliza się czy oddala
wyjscie poza plansze game over
policzyc ruchy porzebne do wygrania

extra:
po osiagnieciu dwukrotnosic min liczby krokow porzebnych do wygrania przeniesc skarb
z prawdopodobienstwem 1/5 nie podawac graczowi wskazowki po ruchu.

"""
import math
from random import randint

def losuj_polozenie():
    losujx = randint(1,10)
    losujy = randint(1,10)

    return losujx, losujy

def pobranie_ruchu(graczx, graczy):

    koniec = False
    ruch = input('Wykonaj ruch [wsad]: ')
    if ruch == 'w':
        graczy += 1
    if ruch == 's':
        graczy -= 1
    if ruch == 'a':
        graczx -= 1
    if ruch == 'd':
        graczx += 1
    # warunki wyjscia poza planszę
    if graczx >10 or graczy >10 or (graczx or graczy) < 0:
        print('Milordzie opuściłeś krainę. Rozgrywka zakończona !!')
        koniec = True
    return graczx, graczy, koniec


def ruch_na_planszy (graczx, graczy, skarbx, skarby, odleglosc_poprzenia,licz_kroki):
   # obliczanie odleglości na planszy z przekatnej prostokąta
    ox = abs(graczx-skarbx)
    oy = abs(graczy-skarby)
    odleglosc = math.sqrt(ox**2 + oy**2)
    
    #generowanie podpowiedzi
    prawdopod = randint(1, 5)
    if prawdopod == 5:
        print ('upss... tym razem nie będzie podpowiedzi jak Ci poszło')
    elif odleglosc < odleglosc_poprzenia:
        print('Jaśnie Panie jesteś bliżej skarbu. ')
    elif odleglosc > odleglosc_poprzenia:
        print ('Jaśnie Panie jesteś dalej od skarbu. ')
    elif odleglosc == odleglosc_poprzenia:
        print ('Jaśnie Panie odleglość od skarbu się nie zmieniła')
  
    # warunek wygrnej
    wygrana = False
    if odleglosc == 0:
        print (f'''
        Zostałeś ozłocony Milordzie, potrzebowałeś {licz_kroki} kroków do odnalezienia złota, 
        niechaj dobrotliwe Gobliny mają Cię w opiece !!''')
        wygrana = True


    return odleglosc, wygrana



def gra():
    #losowanie położenia skarbu i gracza
    skarbx, skarby = losuj_polozenie()
    graczx, graczy = losuj_polozenie()
    print(f"""Witaj w magicznej kranie Goblinów, jedno z pól ukrywa kufer złota. 
    Możesz podjąć się próby odnalezienia skarbu. 
    Plansza ma wymiar kwadratu o wymiarze 10x10. 
    Postępuj zgodnie ze wskazówkami, a może uda Ci się odnaleźć ukryte złoto.
    Twoja pozycja startowa to x: {graczx}, y: {graczy}
    """)

    #mechanika rozgrywki:
    wygrana = 0
    koniec = 0
    odleglosc_poprzednia = 100
    licz_kroki = 1
    while True:
        licz_kroki +=1
        graczx, graczy, koniec = pobranie_ruchu(graczx,graczy)
        odleglosc, wygrana = ruch_na_planszy(graczx,graczy,skarbx,skarby,odleglosc_poprzednia,licz_kroki)
        odleglosc_poprzednia = odleglosc
        if licz_kroki == 15 or licz_kroki == 30:
            skarbx, sklarby = losuj_polozenie()
            print('Panie idzie ci straszne nie poradnie, Gobliny przeniosły skarb w inne miejsce')
#        print (f'wygrana: {wygrana},koniec: kon: {koniec}')
        if wygrana == True or koniec == True:
            break
gra()
