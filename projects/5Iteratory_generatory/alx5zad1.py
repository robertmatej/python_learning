"""
Implement iterator counting from 0 to given limit
for number in Counter(10)
"""

class Counter:

    def __init__(self, i):
        self.i = i
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.j:
            raise StopIteration
        else:
            self.j += 1

        return self.j

#iter = Counter(10)
for number in Counter(4):
    print(number)