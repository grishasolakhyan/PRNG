import numpy as np
import matplotlib.pyplot as plt

class PRNG_methods:
    def __init__(self):
        pass

    def middle_square_method(self, iters):
        X_list = []
        Y_list = []
        a1 = int(input('Enter the number: '))
        for i in range(iters):
            str_a1 = str(a1)
            a1 = int(str_a1)
            a2 = a1**2
            str_a2 = str(a2)

            if len(str_a2) < 8:
                str_a2 = (8 - len(str_a2)) * '0' + str_a2
            print(str_a2)
            str_a2 = str_a2[2:6]
            print(f'{a1} -> {a2} -> {str_a2}')
            a2 = int(str_a2)
            Y_list.append(a2 / 10000)
            X_list.append(i + 1)
            a1 = a2
            if a1 == 0:
                print(f'GENERATION HAS REACHED ZERO!')
                break
        return X_list, Y_list

    def middle_multiplication_method(self, iters):
        X_list = []
        Y_list = []
        a = int(input('Enter the first number: '))
        b = int(input('Enter the second number: '))
        for i in range (iters):
            c = a * b
            str_c1 = str(c)

            if len(str_c1) < 8:
                str_c1 = (8 - len(str_c1)) * '0' + str_c1

            str_c2 = str_c1[2:6]
            c2 = int(str_c2)
            print(f'{a} x {b} = {c}')
            a = b
            b = c2
            X_list.append(i+1)
            Y_list.append(c2/10000)
            if c2 == 0:
                print(f'GENERATION HAS REACHED ZERO!')
                break
        return X_list, Y_list

    def linear_congruential_method(self):
        return 0

    def mixing_method(self):
        return 0

method = PRNG_methods()
#X_list, Y_list = method.middle_square_method(50)
X_list, Y_list = method.middle_multiplication_method(500)

print(X_list)
print(Y_list)

plt.scatter(X_list, Y_list, s=10, c='#007dff')
plt.show()