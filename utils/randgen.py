import random


# class based generator to generate 15 random numbers in range(1,82)
class RandomCharacters:
    def __init__(self):
        self.start = 1
        self.stop = 82

    def __iter__(self):
        for i in range(15):
            yield random.randrange(self.start, self.stop + 1)


# class based generator to generate 3 random numbers in given range
class ThreeRandom:
    def __init__(self, range):
        self.start = range[0]
        self.stop = range[1]

    def __iter__(self):
        for i in range(3):
            yield random.randrange(self.start, self.stop + 1)
