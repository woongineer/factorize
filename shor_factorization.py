import math
import random
import numpy as np
from fractions import Fraction
from qiskit import QuantumCircuit, execute, Aer

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
        if (a ** x) % N == 1:
            return x
    return -1


@timer
def factorize4(N):
    while True:

        a = random.randint(2, N - 1)
        gcd = math.gcd(N, a)

        if gcd != 1:
            return gcd, N // gcd, None

        r, qcs = findPeriodByQuantumCircuit(N, a)
        if r % 2 != 0:
            continue
        gcd1 = math.gcd(N, a ** (r // 2) + 1)
        gcd2 = math.gcd(N, a ** (r // 2) - 1)
        if gcd1 == 1 or gcd2 == 1:
            continue
        return gcd1, gcd2, qcs

def findPeriodByQuantumCircuit(N, a):
    phase, qc = qpe_amod15(a)
    frac = Fraction(phase).limit_denominator(15) # 분모가 15
    return frac.denominator, qc


def qpe_amod15(a):
    n_count = 3
    qc = QuantumCircuit(4 + n_count, n_count)
    for q in range(n_count):
        qc.h(q)
    qc.x(3 + n_count)
    for q in range(n_count):
        qc.append(c_amod15(a, 2 ** q), [q] + [i + n_count for i in range(4)])
    qc.append(qft_dagger(n_count), range(n_count))
    qc.measure(range(n_count), range(n_count))
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1, memory=True).result()
    readings = result.get_memory()
    phase = int(readings[0], 2) / (2 ** n_count)
    return phase, qc


def c_amod15(a, power):
    U = QuantumCircuit(4)
    for iteration in range(power):
        if a in [2, 13]:
            U.swap(0, 1); U.swap(1, 2); U.swap(2, 3)
        if a in [7, 8]:
            U.swap(2, 3); U.swap(1, 2); U.swap(0, 1)
        if a == 11:
            U.swap(1, 3); U.swap(0, 2)
        if a in [7, 11, 13]:
            for q in range(4):
                U.x(q)
    U = U.to_gate()
    U.name = " %i^%i mod 15" % (a, power)
    c_U = U.control()
    return c_U


def qft_dagger(n):
    qc = QuantumCircuit(n)
    for qubit in range(n // 2):
       qc.swap(qubit, n - qubit - 1)
    for j in range(n):
        for m in range(j):
            qc.cp(-np.pi / float(2**(j-m)), m, j)
        qc.h(j)
    qc.name = " QFT† (I-QFT)"

    return qc