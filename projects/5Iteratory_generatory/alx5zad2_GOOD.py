"""
Implement itarator returning vovel
from given string
for char in Vovles(' ala ma kota')
"""

class Vovels:

    def __init__(self, input_):
        self.input_ = input_.lower()
        self.vovels = {'a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y'}
        self.output = ''
        self.input_len = len(input_)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.input_len:
            raise StopIteration

        if self.input_[self.i] in self.vovels:
            self.output = self.input_[self.i]

        if self.input_[self.i] not in self.vovels:
            self.output = ''

        self.i += 1
        return self.output

for char in Vovels('ala ma kota a kot ma ale ĘĘąą'):
    print(char, end = '')
