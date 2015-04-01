__author__ = 'Tony'
import timeit


start = timeit.default_timer()

def diff(maxnum):
    lst1 = []
    lst2 = []
    for e in range(1, maxnum+1):
        lst1.append(e**2)
        lst2.append(e)
    return sum(lst2)**2 - sum(lst1)

print diff(100)



stop = timeit.default_timer()

print stop - start