"""
Zliczyć liczbę unikalnych liczb wprowadzonych przez usera
policzyć ile z nich jest liczbami paryzstymui z zakr 0-100
uzyj iloczynu
"""


zbior = set()
parzyste = set(range(2,101,2))

while True:
    wej = input('Podaj dowolną liczbę, aby wyjść "q"')
    if wej == 'q':
        break
    else:
        zbior.add(int(wej))

print (f'Wprowadzon zbiór {zbior}, jest {len(parzyste & zbior)} parzystych wspólnych: {parzyste & zbior}')


