def check_if_prime(num):
    for a in range(2, num):
        if num % a == 0:
            return False
        else:
            return True


def prime_factors(number):
    prime_fct = []
    for e in range(2, number):
        if number % e == 0:
            prime = check_if_prime(e)
            if prime:
                prime_fct.append(e)
    return prime_fct


print prime_factors(25)