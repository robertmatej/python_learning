class ExtendedFizzBuzzIterator:

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.data = {3: 'Ala', 5: 'ma', 7: 'kota'}

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        for k, v in self.data.items():
            if not self.i % k:
                return v
        return self.i

print([a for a in ExtendedFizzBuzzIterator(10)])  # [1, 2, 'Ala', 4, 'ma', 'Ala', 'kota', 8, 'Ala', 'ma']