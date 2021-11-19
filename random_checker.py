import random


class RandomChecker():
    def __call__(self):
        return random.choice([True, False])
