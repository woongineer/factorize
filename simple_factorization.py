import math
from utils import timer


def add_factor(factors, f):
    if f not in factors:
        factors[f] = 1
    else:
        factors[f] += 1


@timer
def factorize1(n):
    factors = {}
    sqrtn = math.floor(math.sqrt(n))

    for i in range(2, sqrtn + 1):
        while (n % i == 0):
            add_factor(factors, i)
            n = n // i

    if n > 1:
        add_factor(factors, n)

    return factors


def get_mpf(n, mpf):
    if n in mpf:
        return mpf[n]
    else:
        sqrtn = math.floor((math.sqrt(n)))
        for i in range(2, sqrtn + 1):
            if n % i == 0:
                mpf[n] = i
                return i
        mpf[n] = n
        return n


@timer
def factorize2(n):
    mpf = {}
    factors = {}
    while n > 1:
        mpfn = get_mpf(n, mpf)
        add_factor(factors, mpfn)
        n = n // mpfn
    return factors
