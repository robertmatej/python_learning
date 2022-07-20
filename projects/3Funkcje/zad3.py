"""
funkcja licząca liczbę znaków w zadanym napisie pomiędzy zadanymi znacznkami <>
Znaczniki powinny być argumentami z wartościami domyślnymi <>
znaczniki mogą być zagnieżdżone i
zbaki pomiędzy zagnieżdżonymi znacznikami liczone są zgodnie z poziomem zagnieżdźenia ??

"""
def licz_znaki (napis, z_pocz = '<', z_kon = '>'):
    licz = 0
    czy_licze = False
    licz_poziom = 0
    for znak in napis.lower():
        if znak == z_pocz:
            czy_licze = True
            licz_poziom +=1
        if znak == z_kon:
            czy_licze = False
            licz_poziom -=1
        if czy_licze == True: #or licz_poziom > 0:
            licz +=1

    return licz-licz

print(licz_znaki('jakis ><dzi<<<w>n<y> znak tu wystepuje'))