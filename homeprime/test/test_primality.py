import unittest
import numpy as np
from .. import primality

class TestPrimality(unittest.TestCase):

	def setUp(self) -> None:
		primes = np.loadtxt('homeprime/test/primes.txt', dtype=int)
		self.N = int(1e5)
		self.is_prime = np.zeros((self.N,), dtype=bool)
		for p in primes:
			self.is_prime[p] = True

	def test_miller_rabin(self):
		for n in range(2, self.N):
			self.assertTrue(primality.miller_rabin(n) == self.is_prime[n])

	def test_ecpp(self):
		pass
		# for n in range(2, self.N):
		# 	self.assertTrue(primality.miller_rabin(n) == self.is_prime[n])

	def test_is_prime(self):
		for n in range(2, self.N):
			self.assertTrue(primality.is_prime(n) == self.is_prime[n])
