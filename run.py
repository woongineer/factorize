from simple_factorization import factorize1, factorize2
from shor_factorization import factorize3


if __name__ == '__main__':
    n = 3331143123123119
    result = factorize1(n)
    print(f"{n}:{result}")

    result = factorize2(n)
    print(f"{n}:{result}")

    result = factorize3(n)
    print(f"{n}:{result}")
