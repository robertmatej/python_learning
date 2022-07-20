"""
Funkcja obliczająca średnią temperaturę w tygodniu na podstawie temp wpistanych przez usera

"""

def pobranie_temp():
    temp_we = ["pon", "wt", "śr", "czw", 'pt', "sob", "ndz"]
    temp = []
    for i in temp_we:
        temp.append(float(input(f"podaj temperaturę dla dnia {i}: ")))
#    print (temp)
    return temp

def licz_srednia_temp(temp):
        srednia = sum(temp)/len(temp)
        return srednia

def wyswietl():
    temp = pobranie_temp()
    sredia =licz_srednia_temp(temp)

    print(f'średnia temperatura wyniosła: {sredia}: ')

wyswietl()