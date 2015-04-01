__author__ = 'Tony'
import itertools
import timeit


start = timeit.default_timer()

def is_prime(num):
    for i in xrange(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeterm(term):
    count = 0
    for e in itertools.count(2):
        if is_prime(e):
            count += 1
        if count == term:
            return e

print primeterm(10001)

stop = timeit.default_timer()

print stop - start


