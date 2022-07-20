"""
zamioana miejscami element największy z najmniejsyzm, lista jest z góry zadana

"""
lista = [1, 30, 22, -4, 50, 8, 9, 500, 20, 80, 77, 55, 22, 900]
najmniejsza = None
najwieksza = None
i = 0
print(f'lista przed zmianą {lista}')
for szuka in lista:

    if najmniejsza == None or szuka < najmniejsza:
        najmniejsza  = szuka
        indeks_min = i
    if najwieksza == None or szuka > najwieksza:
        najwieksza = szuka
        indeks_max = i
    i += 1
lista[indeks_min] = najwieksza
lista[indeks_max] = najmniejsza
#lista2 = lista.insert(indeks_min,najwieksza)
#lista2= lista.del[indeks_min+1]
print(f"najwieksza: {najwieksza},"f" najmniejsza: {najmniejsza} \n"
      f"lista po zmianie {lista}")

#sprawdzenie czy wynik jest poprawny
assert lista == [1, 30, 22, 900, 50, 8, 9, 500, 20, 80, 77, 55, 22, -4]