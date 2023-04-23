from shor_factorization import factorize3, factorize4
from simple_factorization import factorize1, factorize2

if __name__ == '__main__':
    n = 3331143123123119
    n = 7 * 11
    # n = 229 * 241
    result = factorize1(n)
    print(f"{n}:{result}")

    result = factorize2(n)
    print(f"{n}:{result}")

    result = factorize3(n)
    print(f"{n}:{result}")

    p, q, qc = factorize4(n)


    print(f"{n}:{p, q}")

    if qc != None:
        qc.draw()
    else:
        print('it was none')
