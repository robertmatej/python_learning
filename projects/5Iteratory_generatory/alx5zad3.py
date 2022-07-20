"""
Implement generator returning vovel
from given string
for char in vovles(' ala ma kota')
"""

def vovles(string):

    vovels = {'a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y'}

    for char in string.lower() :
        if char in vovels:
            yield char


for data in vovles('Ala śpi pod płotem ponieważ jest ciepło'):
    print(data)

print()
vol = vovles('Grześ śpi pod płotem')
print(vol.__next__())
print(next(vol))