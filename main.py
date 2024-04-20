import numpy as np
import random
import math
import matplotlib.pyplot as plt
import pylab
class Zero(Exception): pass
class NegativeNumber(Exception): pass
class NonFourDigitNumber(Exception): pass
class NonEightDigitNumber(Exception): pass

N = 2000
n = int(N/2)

class PRNG_methods:
    def __init__(self):
        pass

    def fix_loop(self, Y_list, check_value):
        check = True
        while (check == True):
            val = check_value / 10000
            if (val in Y_list):
                check_value += 1
            elif (val not in Y_list):
                check = False
        return check_value

    def fix_zero(self, check_value):
        num_zeros = check_value.count('0')
        if num_zeros > 2:
            check_value = check_value.replace("0", "1")
        return check_value


    def middle_square_method(self, iters):
        main_list = []
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
            str_a2 = str_a2[2:6]

            str_a_0 = self.fix_zero(str_a2)
            a2 = int(str_a_0)

            a2 = self.fix_loop(main_list, a2)
            main_list.append(a2 / 10000)
            a1 = a2

            if a1 == 0:
                print(f'GENERATION HAS REACHED ZERO!')
                break

        for i in range(n):
            X_list.append(main_list[i])
            Y_list.append(main_list[N - i - 1])

        return main_list, X_list, Y_list

    def middle_multiplication_method(self, iters):
        main_list = []
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

            str_c_0 = self.fix_zero(str_c2)
            c2 = int(str_c_0)

            c2 = self.fix_loop(main_list, c2)
            main_list.append(c2 / 10000)

            a = b
            b = c2

            if c2 == 0:
                print(f'GENERATION HAS REACHED ZERO!')
                break

        for i in range(n):
            X_list.append(main_list[i])
            Y_list.append(main_list[N - i - 1])

        return main_list, X_list, Y_list

    def mixing_method(self, iters):
        main_list = []
        X_list = []
        Y_list = []

        a = int(input(f'Enter 8-digit number: '))

        if a == 0:
            raise Zero()
        elif a < 0:
            raise NegativeNumber()
        elif len(str(a)) != 8:
            raise NonEightDigitNumber()
        for i in range(iters):
            str_a = str(a)

            str_a_right = ''
            str_a_right = str_a_right + str_a[6:] + str_a[0:6]

            str_a_left = ''
            str_a_left = str_a_left + str_a[2:] + str_a[0:2]

            a_right = int(str_a_right)
            a_left = int(str_a_left)

            c = a_right + a_left
            str_c = str(c)
            str_c2 = ''
            if (len(str_c) > 8):
                str_c2 = str_c[1:]
            else:
                str_c2 = str_c
            a = int(str_c2)

            main_list.append(a / 10**8)

            if a == 0:
                print(f'GENERATION HAS REACHED ZERO!')
                break

        for i in range(n):
            X_list.append(main_list[i])
            Y_list.append(main_list[N - i - 1])

        return main_list, X_list, Y_list

    def linear_congruential_method(self, iters):
        main_list = []
        X_list = []
        Y_list = []

        m = 2 ** 32
        a = 268435461
        b = 907612489
        X0 = int(input(f'Enter the number: '))
        for i in range(iters):
            X1 = math.ceil(math.fmod((a * math.ceil(X0) + b), m))
            X0 = X1

            main_list.append(X0 * 2.3 / 10 ** 10)

        for i in range(n):
            X_list.append(main_list[i])
            Y_list.append(main_list[N - i - 1])

        return main_list, X_list, Y_list

def frequency_analysis_method(arr, n):
    steps = int(input(f'Enter the number of steps: '))

    if steps == 0:
        raise Zero()
    elif steps < 0:
        raise NegativeNumber()

    st = 1 / steps
    s_t0 = -st
    s_t1 = 0

    freq_arr = []
    ind = []

    for i in range(steps):
        s_t0 = s_t0 + st
        s_t1 = s_t1 + st
        k = 0
        for j in range(len(arr)):
            if (s_t0 < arr[j] <= s_t1):
                k = k + 1
        freq_arr.append(k)

    for i in range(len(freq_arr)):
        freq_arr[i] = (freq_arr[i] / n) * 100
        ind.append(i + 1)

    return freq_arr, ind

def correlation(main_list):
    ind2=[]
    R=[]
    for i in range(1,n):
        ter=[]
        for j in range(i):
            ter.append(main_list[j]*main_list[j+1])
        R.append((sum(ter)/i)*12-3)
        ind2.append(i)
    return R, ind2


def expected_value_and_variance(final_array):
    sum_m = 0
    M = sum(final_array) / N  # expected value

    mid_final_array = np.mean(final_array)
    for i in range(len(final_array)):
        sum_m = sum_m + (mid_final_array - final_array[i]) ** 2
    D = sum_m / N  # variance
    return M, D

class Graph:
    def __init__(self):
        pass

    def scatter(self, title, x, y, rand1, rand2, freq_arr, ind, corr_arr, ind2):
        str_N = str(N)
        figure, axis = plt.subplots(2, 2)

        axis[0, 0].scatter(x, y, s=8, c='#007dff')
        axis[0, 0].set_title(title + ' at N=' + str_N)
        axis[0, 0].set_xlabel('r')
        axis[0, 0].set_ylabel('r=f(y)')

        axis[0, 1].scatter(rand1, rand2, s=8, c='red')
        axis[0, 1].set_title('rand()' + ' at N=' + str_N)
        axis[0, 1].set_xlabel('r')
        axis[0, 1].set_ylabel('r=f(y)')

        axis[1, 0].plot(ind, freq_arr, c='blue')
        axis[1, 0].set_title('Frequency analysis' + ' at N=' + str_N)
        axis[1, 0].set_ylabel('fi, %')

        axis[1, 1].plot(ind2, corr_arr, c='orange')
        axis[1, 1].set_title("Correlation" + ' at N=' + str_N)

        plt.show()

        return 0

def randomize(iters):
    rand = []
    rand1 = []
    rand2 = []

    for i in range(iters):
        rand.append(random.randint(0, 9999))
        rand[i] = rand[i] / 10000
    for i in range(n):
        rand1.append(rand[i])
        rand2.append(rand[iters - i - 1])

    return rand1, rand2

number_operation = ''
while(number_operation != '0'):
    number_operation = input(
        f'1) Middle square method\n'
        f'2) Middle multiplication method\n'
        f'3) Mixing method\n'
        f'4) Linear congruential method\n'
        f'0) Quit\n\n'
        f'Choose the operation: ')

    if(number_operation == '1'):
        method = PRNG_methods()
        try:
            main_list, X_list, Y_list = method.middle_square_method(N)
            rand1, rand2 = randomize(N)
            frequency_array, ind = frequency_analysis_method(X_list, n)
            correlation_array, ind2 = correlation(main_list)
            M, D = expected_value_and_variance(main_list)
            title = 'Middle square method'

            plot_graph = Graph()
            plot_graph.scatter(title, X_list, Y_list, rand1, rand2, frequency_array, ind, correlation_array, ind2)
            print(f'{M} and {D}')

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
            main_list, X_list, Y_list = method.middle_multiplication_method(N)
            rand1, rand2 = randomize(N)
            frequency_array, ind = frequency_analysis_method(X_list, n)
            correlation_array, ind2 = correlation(main_list)
            title = 'Middle multiplication method'

            plot_graph = Graph()
            plot_graph.scatter(title, X_list, Y_list, rand1, rand2, frequency_array, ind, correlation_array, ind2)

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
            main_list, X_list, Y_list = method.mixing_method(N)
            rand1, rand2 = randomize(N)
            frequency_array, ind = frequency_analysis_method(X_list, n)
            correlation_array, ind2 = correlation(main_list)
            title = 'Mixing method'

            plot_graph = Graph()
            plot_graph.scatter(title, X_list, Y_list, rand1, rand2, frequency_array, ind, correlation_array, ind2)

        except Zero:
            print(f'Wrong number: Zero!\n')
        except NegativeNumber:
            print(f'Wrong number: Negative number!\n')
        except NonEightDigitNumber:
            print(f'Wrong number: Not a 8-digit number!\n')

    elif(number_operation == '4'):
        method = PRNG_methods()

        main_list, X_list, Y_list = method.linear_congruential_method(N)
        rand1, rand2 = randomize(N)
        frequency_array, ind = frequency_analysis_method(X_list, n)
        correlation_array, ind2 = correlation(main_list)
        title = 'Linear congruential method'

        plot_graph = Graph()
        plot_graph.scatter(title, X_list, Y_list, rand1, rand2, frequency_array, ind, correlation_array, ind2)

    elif(number_operation == '0'):
        quit()

    else:
        print(f'Unknown number of operation.\n')