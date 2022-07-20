""""
sklep 2.0, podać cenę na podstawie wpisanych nazw produktu, wyświetlić cały asortyment sklepu
użyć słownika
"""
sklep = {'ziemniaki': 1.4, 'cebula': 1.8, 'kapusta': 2, 'marchew': 3.5, 'pomidor': 6.5, 'banan': 4.6, 'sałata': 3.5, 'jabłko': 4.2, 'ogórek': 5.3, 'wiśnie': 6.4, 'czereśnie': 14.1, 'gruszka': 4.8, 'arbuz':5.2}

print (f'w ofercie mamy nastęujące produkty{sklep}')
cena = float()
rachunek = []

while True:
    zakupy = input('Co podać? Jeżeli kończymy wybierz "q" ')
    if zakupy == "q":
        break
    for i in sklep:
        if zakupy == i:
            waga = int(input(f'ile {i} zważyć? '))
            rachunek.append(sklep[i]*waga)
        # else:
        #     print ('Nie posiadamy takiego produktu')


print (f'Kwota do zapłaty: {sum(rachunek)} PLN ')