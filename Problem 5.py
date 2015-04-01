__author__ = 'Tony'

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import itertools
import timeit


start = timeit.default_timer()

def is_divisible(maxnum):
    for e in itertools.count(1):
        if all(e % f == 0 for f in range(11,maxnum+1)):
            return e

print is_divisible(20)

stop = timeit.default_timer()


print stop - start
