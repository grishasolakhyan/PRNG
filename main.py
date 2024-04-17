import numpy as np
import matplotlib.pyplot as plt

class PRNG_methods:
    def __init__(self):
        pass

    def middle_square_method(self, x):
        str_x = str(x)
        x = int(str_x)
        x2 = x**2
        str_x2 = str(x2)

        if len(str_x2) < 8:
            str_x2 = (8 - len(str_x2)) * '0' + str_x2
        print(str_x2)
        str_x2 = str_x2[2:6]
        print(f'{x} -> {x2} -> {str_x2}')
        x2 = int(str_x2)
        return x2

    def middle_multiplication_method(self):
        return 0

    def linear_congruential_method(self):
        return 0

    def mixing_method(self):
        return 0

msm_list = []
msm_ind = []
method = PRNG_methods()
num = int(input('Enter the number: '))

for i in range(100):
    res = method.middle_square_method(num)
    msm_list.append(res/10000)
    msm_ind.append(i+1)
    num = res
    if num == 0:
        print(f'GENERATION HAS REACHED ZERO!')
        break

print(msm_ind)
print(msm_list)

plt.scatter(msm_ind, msm_list, s=10, c='#007dff')
plt.show()