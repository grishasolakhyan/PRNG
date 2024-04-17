import numpy as np
import matplotlib.pyplot as plt
class Zero(Exception): pass
class NegativeNumber(Exception): pass
class NonFourDigitNumber(Exception): pass
class NonEightDigitNumber(Exception): pass

class PRNG_methods:
    def __init__(self):
        pass

    def checking(self, check_value):
        return 0

    def middle_square_method(self, iters):
        X_list = []
        Y_list = []
        a1 = int(input('Enter the 4-digit number: '))

        if a1 == 0:
            raise Zero()
        elif a1 < 0:
            raise NegativeNumber()
        elif len(str(a1)) != 4:
            raise NonFourDigitNumber


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
        a = int(input('Enter the first 4-digit number: '))
        b = int(input('Enter the second 4-digit number: '))

        if a == 0 or b == 0:
            raise Zero()
        elif a < 0 or b < 0:
            raise NegativeNumber()
        elif len(str(a)) != 4 or len(str(b)) != 4:
            raise NonFourDigitNumber()

        for i in range (iters):
            c1 = a * b
            str_c1 = str(c1)

            if len(str_c1) < 8:
                str_c1 = (8 - len(str_c1)) * '0' + str_c1

            str_c2 = str_c1[2:6]
            c2 = int(str_c2)
            print(f'{a} x {b} = {c1}')
            a = b
            b = c2
            X_list.append(i+1)
            Y_list.append(c2/10000)
            if c2 == 0:
                print(f'GENERATION HAS REACHED ZERO!')
                break
        return X_list, Y_list

    def mixing_method(self, iters):
        X_list = []
        Y_list = []
        a = int(input(f'Enter 8-digit number: '))

        if a == 0:
            raise Zero()
        elif a < 0:
            raise NegativeNumber()
        elif len(str(a)) != 8:
            raise NonEightDigitNumber()

        str_a = str(a)

        str_a_right = ''
        str_a_right = str_a_right + str_a[6:] + str_a[0:6]

        str_a_left = ''
        str_a_left = str_a_left + str_a[2:] + str_a[0:2]

        print(f'{str_a} -> {str_a_right} and {str_a_left}')

        return 0

    def linear_congruential_method(self):
        return 0

number_operation = ''
while(number_operation != '0'):
    number_operation = input(
        f'1) Middle square method\n'
        f'2) Middle multiplication method\n'
        f'3) Mixing method\n'
        f'4) Linear congruential method\n'
        f'0) Quit\n'
        f'Choose the operation: ')
    N = 50

    if(number_operation == '1'):
        method = PRNG_methods()
        try:
            X_list, Y_list = method.middle_square_method(N)

            print(X_list)
            print(Y_list)

            plt.scatter(X_list, Y_list, s=10, c='#007dff')
            plt.show()

        except Zero:
            print(f'Wrong number: Zero!\n')
        except NegativeNumber:
            print(f'Wrong number: Negative number!\n')
        except NonFourDigitNumber:
            print(f'Wrong number: Not a 4-digit number!\n')


    elif(number_operation == '2'):
        method = PRNG_methods()
        X_list = []
        Y_list = []

        try:
            X_list, Y_list = method.middle_multiplication_method(N)

            print(X_list)
            print(Y_list)

            plt.scatter(X_list, Y_list, s=10, c='#007dff')
            plt.show()

        except Zero:
            print(f'Wrong number: Zero!\n')
        except NegativeNumber:
            print(f'Wrong number: Negative number!\n')
        except NonFourDigitNumber:
            print(f'Wrong number: Not a 4-digit number!\n')

    elif(number_operation == '3'):
        method = PRNG_methods()
        X_list = []
        Y_list = []
        try:
            method.mixing_method(N)

            # print(X_list)
            # print(Y_list)
            #
            # plt.scatter(X_list, Y_list, s=10, c='#007dff')
            # plt.show()

        except Zero:
            print(f'Wrong number: Zero!\n')
        except NegativeNumber:
            print(f'Wrong number: Negative number!\n')
        except NonEightDigitNumber:
            print(f'Wrong number: Not a 8-digit number!\n')

    elif(number_operation == '4'):
        method = PRNG_methods()
        X_list = []
        Y_list = []

    elif(number_operation == '0'):
        quit()

    else:
        print(f'Unknown number of operation.\n')