from math import ceil, gcd, log
from random import randint

from .ec import elliptic_curve


def is_prime(n: int):
    """
    Returns True if n is prime, and False if composite.

    Uses Miller-Rabin test in the first round. If n passes Miller-Rabin (n is
    probably prime) then elliptic curve primality testing is used.
    """

    # check for valid input
    if type(n) != int:
        TypeError("n must be an integer at least 2")
    if n < 2:
        ValueError("n must be an integer at least 2")

    # n fails the Miller-Rabin test iff n is composite
    if not miller_rabin(n):
        return False

    # passes Miller-Rabin, n is probably prime, use ECPP to validate
    return ecpp(n)


def miller_rabin(n: int, tol=1e-16):
    """
    Applies the Miller-Rabin test t times,
    where t is sufficiently large enough to ensure that
    a false positive has probability of less than tol > 0
    """

    # if n = 2 or 3, then n is prime
    if n == 2 or n == 3:
        return True

    # check if divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # number of times to apply the Miller-Rabin test
    t = ceil(log(log(n) / tol) / log(4))

    for _ in range(t):
        a = randint(2, n - 1)
        if not miller_rabin_check_witness(n, a):
            # n is composite
            return False

    # otherwise, n passes the Miller-Rabin test t times (probably prime)
    return True


def miller_rabin_check_witness(n: int, a: int):
    """
    Miller-Rabin compositeness test for the witness a
    returns False for composite
    returns True if test fails (probably prime)
    """
    g = gcd(a, n)
    if 1 < g < n:
        # g divides n, so n is not prime
        return False
    q = n - 1
    k = 0
    while q % 2 == 0:
        q = q // 2
        k += 1
    a = pow(a, q, n)
    if a == 1:
        # Converse of Fermat's Little Theorem: n is probably prime
        return True
    for _ in range(k):
        if (a + 1) % n == 0:
            # probably prime
            return True
        a = (a * a) % n
    # n is definitely composite
    return False


def ecpp(n: int):
    """
    Elliptic curve primality testing

    Returns True if and only if n is prime
    """

    # if n = 2 or 3, then n is prime
    if n == 2 or n == 3:
        return True

    # check if divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    e = elliptic_curve()

    return True
