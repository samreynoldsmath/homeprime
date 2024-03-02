
# # import numpy as np

# from ..factor import factor


# class TestFactor(unittest.TestCase):
#     def setUp(self) -> None:
#         primes = np.loadtxt("homeprime/test/primes.txt", dtype=int)
#         self.N = int(1e5)
#         # self.is_prime = np.zeros((self.N,), dtype=bool)
#         # for p in primes:
#         #     self.is_prime[p] = True
#         self.is_prime = []

#     def test_factor(self):
#         for n in range(2, self.N):
#             f = factor(n)
#             self.assertTrue(f.success)
#             for p in f.factors:
#                 self.assertTrue(self.is_prime[p])

import os
import sys

sys.path.append("..")

import homeprime

def load_primes(max_n: int) -> set[int]:
    """Load primes from file."""
    filename = os.path.join(os.path.dirname(__file__), "primes.txt")
    primes = set()
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            p = int(line)
            if p > max_n:
                break
            primes.add(p)
    return set(primes)

def test_factor():
    """Test factorization."""
    max_n = 100_000
    primes = load_primes(max_n)
    for n in range(2, max_n):
        f = homeprime.factor.factor(n)
        assert f.success
        for p in f.factors:
            assert p in primes
