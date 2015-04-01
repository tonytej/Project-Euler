from operator import mul
import timeit



start = timeit.default_timer()

def is_prime(num):
    for i in xrange(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primetill(num):
    lst = []
    for e in range(2,num):
        if is_prime(e):
            lst.append(e)
    return lst

def problem5(num):
    primelist = primetill(num)
    for e in primelist:
        n = 0
        f = 1
        g = e
        while f <= num:
            f = e**(2+n)
            n += 1
            if f <= num:
                primelist[primelist.index(g)] = f
                g = f
    return reduce(mul, primelist)
print problem5(20)

stop = timeit.default_timer()

print stop - start

