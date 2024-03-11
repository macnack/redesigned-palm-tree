import time
import timeit

import numpy as np


# 1. the simplest usage
print("1. the simplest usage")
print(timeit.timeit('[(a, b) for a in (1,3,5) for b in (2,4,6)]', number=1))
print(np.mean(timeit.repeat('[(a, b) for a in (1,3,5) for b in (2,4,6)]', repeat=5, number=1)))


def test_func_1():
    s = 0.0
    for i in range(1000):
        s += round(pow(i, 1/2), 2)
        time.sleep(0.01)


# 2. test of a non-parametrized function
print("2. test of a non-parametrized function")
print(np.mean(timeit.repeat(test_func_1, repeat=5, number=1)))


def test_func_2(n):
    s = 0.0
    for i in range(n):
        s += round(pow(i, 1/2), 2)
        time.sleep(0.01)


setup = '''
from __main__ import test_func_2
n = 1000
'''

# 3. test of a parametrized function
print("3. test of a parametrized function")
print(np.mean(timeit.repeat('test_func_2(n)', setup=setup, repeat=5, number=1)))