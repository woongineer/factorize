import math
import random

from utils import timer


@timer
def factorize3(N):
    while True:

        a = random.randint(2, N - 1)
        gcd = math.gcd(N, a)

        if gcd != 1:
            return gcd, N // gcd

        r = find_period(N, a)
        if r % 2 != 0:
            continue
        gcd1 = math.gcd(N, a ** (r // 2) + 1)
        gcd2 = math.gcd(N, a ** (r // 2) - 1)
        if gcd1 == 1 or gcd2 == 1:
            continue
        return gcd1, gcd2


def find_period(N, a):
    for x in range(1, N):
        return x if (a ** x) % N == 1 else -1
