"""
Program zliczający wystąienie liczb dodatnich i ujemnych w zadanej liście liczb całkowitych
"""

lista = [-1, 2, -34, 2, 5, 653, -34, -664, -3442, 43224, -8, -723, - 643, 33, -1, -0, +0]

licz_minus = 0
licz_plus = 0
for licz in lista:
#    print (licz)
    if licz > 0:
        licz_plus += 1
    if licz < 0:
        licz_minus += 1

print (f'w liście znajduje się {licz_minus} liczb -, oraz {licz_plus} liczb + ')