import unittest
import numpy as np
from ..primality import probably_prime

class TestPrimality(unittest.TestCase):

	def setUp(self) -> None:
		primes = np.loadtxt('homeprime/test/primes.txt', dtype=int)
		self.N = int(1e5)
		self.is_prime = np.zeros((self.N,), dtype=bool)
		for p in primes:
			self.is_prime[p] = True

	def test_primality(self):
		for n in range(2, self.N):
			self.assertTrue(probably_prime(n) == self.is_prime[n])