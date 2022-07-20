"""
pobrać do 10 liczb, przechować w liście
zsummowac wartości
"""

a = list ()
i = 0
while True:
    wej = (input(f"Wprowadź do 10 liczb, abywyjśc 'q' {i+1}: "))

    if wej == "q":
        break
    if i == 9:
        break
    else:
        a.append(int(wej))
    i += 1
print(f'Suma: {sum((a))}: ')