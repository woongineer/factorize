from simple_factorization import factorize1, factorize2


if __name__ == '__main__':
    n = 33311431423123119
    result = factorize1(n)
    print(f"{n}:{result}")

    result = factorize2(n)
    print(f"{n}:{result}")
