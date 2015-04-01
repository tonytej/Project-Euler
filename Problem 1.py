import timeit


start = timeit.default_timer()

def problem1(max_num): return sum([e for e in range(1,max_num) if e % 3 == 0 or e % 5 == 0])

print problem1(1000)

stop = timeit.default_timer()

print stop - start



