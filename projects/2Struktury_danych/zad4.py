'''
liczby podzielne przez 3 lub przez 5 z zakresu 0-100
wyświetlićż i polizyć

'''
zakres = range (1,101)
licz_ile = 0
print ('liczby podzielne przez 3 lub przez 5 z zakresu 0-100: ')
for test in zakres:

    if test %3 ==0 or test %5 == 0:
        licz_ile +=1
        print(test)

print(f'w sumie mamy {licz_ile} takich liczb')