class GeomProgress:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    def __next__(self):
        self.start *= 5

        if self.start > self.stop:
            raise StopIteration
        else:
            return self.start

    def __iter__(self):
        return self

gen = GeomProgress(1, 100000)

for a in gen:
    print(a)
