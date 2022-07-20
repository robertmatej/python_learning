"""
program obliczający kwotę za zakupy na podstawie cenyu oraz wagi zakupionych towarow
wyistać info na konsolę
"""

def sklep(cena, waga):

    koszt = cena * waga
    return koszt

def wydruk(cena, waga):
    do_zaplaty = sklep(cena, waga)
    #print(f'do zapłaty za: {waga}kg, po {cena}zł/kg :{round(do_zaplaty,2)}zł ')
    out = f'''do zapłaty za: {waga}kg, 
            w cenie: {cena}zł/kg
            :{round(do_zaplaty,2)}zł'''

    return out

def test_wydruk ():
    assert wydruk (2.3, 2) == f"""do zapłaty za: 2kg, 
            w cenie: 2.3zł/kg
            :4.6zł"""
