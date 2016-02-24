class fibonacci_sequence:
    def __init__(self, a):
        self.i = 1
        self.j = a
        self.d1 = 0
        self.d2 = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.j:
            self.count += 1
            self.d1, self.d2 = self.d2, self.d1 + self.d2
            return self.d1
        else:
            raise StopIteration
        self.count += 1
