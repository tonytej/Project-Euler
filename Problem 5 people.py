from collections import defaultdict

def smallest_number_divisible(start, end):    
    '''
        Function that calculates LCM of all the numbers from start to end
        It breaks each number into it's prime factorization, 
        simultaneously keeping track of highest power of each prime number
    '''
    # Dictionary to store highest power of each prime number.
    prime_power = defaultdict(int)

    for num in xrange(start, end + 1):
        # Prime number generator to generate all primes till num
        prime_gen = (each_num for each_num in range(2, num + 1) if is_prime(each_num))

        # Iterate over all the prime numbers
        for prime in prime_gen:
            # initially quotient should be 0 for this prime numbers
            # Will be increased, if the num is divisible by the current prime
            quotient = 0

            # Iterate until num is still divisible by current prime
            while num % prime == 0:
                num = num / prime
                quotient += 1

            # If quotient of this priime in dictionary is less than new quotient,
            # update dictionary with new quotient
            if prime_power[prime] < quotient:
                prime_power[prime] = quotient

    # Time to get product of each prime raised to corresponding power  
    product = 1

    # Get each prime number with power
    for prime, power in prime_power.iteritems():
        product *= prime ** power

    return product 


def is_prime(num):
    '''
        Function that takes a `number` and checks whether it's prime or not
        Returns False if not prime
        Returns True if prime
    '''
    for i in xrange(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    print smallest_number_divisible(1, 20)

    import timeit
    t = timeit.timeit

    print t('smallest_number_divisible(1, 20)', 
             setup = 'from __main__ import smallest_number_divisible', 
             number = 100)