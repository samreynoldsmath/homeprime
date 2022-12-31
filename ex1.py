"""
Example 1

Find the home primes of each composite number from 4 to 48
"""

from homeprime.homeprime import homeprime
from homeprime.primality import probably_prime

def main():
	for n in range(4, 49):
		if not probably_prime(n):
			homeprime(n, verbose=True)

if __name__ == '__main__':
	main()