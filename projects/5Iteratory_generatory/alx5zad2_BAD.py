"""
Implement itarator returning vovel
from given string
for char in Vovles(' ala ma kota')
Iteratoror nie działa peętlą poza iteratorem a w zasadzie cała praca wykonana w next za pomocą FOR
"""

class Vovels:

    def __init__(self, input_):
        self.input_ = input_
        self.vovels = {'a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y'}
        self.output = []
        self.input_len = len(input_)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        for char in self.input_:
            if self.i == self.input_len:
                raise StopIteration
            if char in self.vovels:
                self.output.append(char)
            self.i += 1

        return self.output


for char in Vovels('ala ma kota a kot ma ale'):
    print(char)
