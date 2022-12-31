from random import randint
from math import log, ceil, gcd

def probably_prime(N, tol=1e-10):
	"""
	Applies the Miller-Rabin test t times,
	where t is sufficiently large enough to ensure that
	a false positive has probability of less than tol > 0
	"""
	if N == 2 or N == 3:
		return True

	# number of times to apply the Miller-Rabin test
	t = ceil(log(log(N) / tol) / log(4))

	for _ in range(t):
		a = randint(2, N - 1)
		if not miller_rabin(N, a):
			# N is composite
			return False

	# otherwise, N passes the Miller-Rabin test t times (probably prime)
	return True

def miller_rabin(N, a):
	"""
	Miller-Rabin test
	returns False for composite
	returns True if test fails (probably prime)
	"""
	g = gcd(a,N)
	if 1 < g and g < N:
		return False

	# write N-1 = 2^k * q for odd q
	q = N - 1
	k = 0
	while q % 2 == 0:
		q = q // 2
		k += 1

	a = pow(a, q, N)
	if a == 1:
		return True

	for _ in range(k):
		if (a + 1) % N == 0:
			return True
		a = (a * a) % N
	return False