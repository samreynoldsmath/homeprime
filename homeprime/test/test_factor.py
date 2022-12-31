import unittest
import numpy as np
from ..factor import factor

class TestFactor(unittest.TestCase):

	def setUp(self) -> None:
		primes = np.loadtxt('homeprime/test/primes.txt', dtype=int)
		self.N = int(1e5)
		self.is_prime = np.zeros((self.N,), dtype=bool)
		for p in primes:
			self.is_prime[p] = True

	def test_factor(self):
		for n in range(2, self.N):
			f = factor(n)
			self.assertTrue(f.success)
			for p in f.factors:
				self.assertTrue(self.is_prime[p])