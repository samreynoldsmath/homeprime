from math import gcd
from random import randint
from . import primality

class factorization:
	"""
	Object to hold prime factors

	Contains methods to do basic checks verifying that the factorization
	calculation was performed correctly, as well as a sort method.
	"""
	def __init__(self, n: int) -> None:
		if type(n) != int:
			TypeError('n must be an integer at least 2')
		if n < 2:
			ValueError('n must be an integer at least 2')
		self.n = n
		self.unfactored_part = n
		self.factors = []
		self.num_factors = 0
		self.success = False

	def set_factor(self, p: int) -> None:
		"""
		Determine if p is a factor, and if it is, add to factor list.

		If a power of p is a factor, say p^a, then a copies of p are
		added to the factor list.
		"""
		if p > 1:
			while self.unfactored_part % p == 0:
				self.factors.append(p)
				self.num_factors += 1
				self.unfactored_part = self.unfactored_part // p
		self.check_success()

	def check_success(self) -> None:
		"""Check all conditions of factor list"""
		is_nontrivial = self.check_factors_nontrivial()
		is_product = self.check_factors_product()
		self.success = is_nontrivial and is_product

	def check_factors_nontrivial(self) -> bool:
		"""Check all factors are > 1"""
		ok = True
		for p in self.factors:
			ok = p > 1 and ok
		return ok

	def check_factors_product(self) -> bool:
		"""Check factors multiply to n"""
		m = 1
		for p in self.factors:
			if p > 1:
				m *= p
		return m == self.n

	def sort(self) -> None:
		"""Sort the factors in ascending order"""
		self.factors.sort()

	def __repr__(self) -> str:
		msg = f'factors of {self.n}\n'
		msg += f'success flag = {self.success}\n'
		msg += f'unfactored part = {self.unfactored_part}\n'
		msg += f'{self.num_factors} factor(s) found: ['
		for p in self.factors:
			msg += f'{p}, '
		msg += ']'
		return msg

def factor(n: int) -> factorization:
	"""
	Returns a sorted list of the prime factors of n, including repeats.

	Currently using Pollard's rho algorithm. This is a suboptimal choice when
	factoring integers without relatively small prime factors.
	"""

	# object to hold prime factors
	f = factorization(n)

	# find factors of 2
	f.set_factor(2)

	# Pollard's rho algorithm
	while not f.success:
		m = f.unfactored_part
		if primality.is_prime(m):
			# if remaining part to be factored is prime, we are done
			f.set_factor(m)
		else:
			# factor the remaining part with Pollard's rho
			p = _get_single_factor_pollard(m)
			if primality.is_prime(p):
				# include only prime factors in the list
				f.set_factor(p)
			else:
				# this recursion is untasteful
				g = factor(p)
				for q in g.factors:
					f.set_factor(q)

	# sort list of factors in ascending order
	f.sort()

	return f

def _get_single_factor_pollard(n: int) -> int:
	"""
	Returns a single factor of n (odd and composite) using Pollard's rho method
	"""
	factor_found = False
	while not factor_found:
		c = randint(1, n - 1)
		x = randint(1, n - 1)
		y = x
		d = 1
		while d == 1:
			# x_{k+1} = f(x_k)
			x = _pollard_mixing_func(x, c, n)

			# y_{k+1} = f(f(y_k))
			y = _pollard_mixing_func(y, c, n)
			y = _pollard_mixing_func(y, c, n)

			# candidate factor
			d = gcd(abs(x - y), n)
		if d < n:
			factor_found = True
	return d

def _pollard_mixing_func(x, c, n):
	"""Mixing polynomial for Pollard's rho algorithm: x^2+c (mod n)"""
	return (x * x + c) % n