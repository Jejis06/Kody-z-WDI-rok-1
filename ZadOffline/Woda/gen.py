from math import gcd
import random

MIN_C = 1
MAX_C = 10000

MIN_N = 3 
MAX_N = 60

def gcd_arr(arr):
    g = arr[0]
    for x in arr:
        g = gcd(x, g)
    return g == 1

def gen_arr(N):
    test_arr = []
    for i in range(N) :
        x = random.randint(MIN_C, MAX_C)
        test_arr.append(x)
    return test_arr

def gen(N):
    test = {}
    test['N'] = N

    test_arr = gen_arr(N)
    # while not gcd_arr(test_arr):
    #     test_arr = gen_arr(N)

    test['arr'] = test_arr
    return test

def get_test():
    N = random.randint(MIN_N, MAX_N)
    test = gen(N)
    return test

if __name__ == '__main__':
    test = get_test()
    print(test['N'])
    print(' '.join(str(i) for i in test['arr']))


    
    

