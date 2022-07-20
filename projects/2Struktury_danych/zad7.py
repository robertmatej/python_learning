"""
Sprawdzić wystąpienie samogłosek a o e i u y w podanym przez usera napisie.
"""

napis = str(input('podaj napis sprawdzimy ile w nim wystepuje samoglosek: '))
licz = 0
for i in napis:
    if i == 'a' or i == 'o' or i == 'e' or i == 'i' or i == 'u' or i == 'y':
        licz +=1

print (f""" w podanym ciągu mamy {licz} samogłosek
             

""")