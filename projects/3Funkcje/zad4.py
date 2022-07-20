"""
Zaimplemnetować funkcję formatującą tekst
podmieania "$cena" na zmienną cena o konkretnej wartośći
"""
def formatuj(text1= 'koszt $cena PLN ',text2 = 'kwota $cena brutto', cena = 10 ):
    t1 = text1.replace('$cena', str(cena))
    t2 = text2.replace('$cena', str(cena))

    return(print(t1+t2))

formatuj()

