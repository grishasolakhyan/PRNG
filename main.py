import numpy as np

class PRNG_methods:
    def __init__(self):
        pass

    def middle_square_method(self, x):
        x2 = x**2
        return x2

    def middle_multiplication_method(self):
        return 0

    def linear_congruential_method(self):
        return 0

    def mixing_method(self):
        return 0

method = PRNG_methods()
num = int(input('Enter the number: '))
res = method.middle_square_method(num)
print(res)