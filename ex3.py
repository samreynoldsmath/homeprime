"""
Example 3

Plots of home prime distribution of composite numbers
"""

import matplotlib.pyplot as plt
import numpy as np
from homeprime.homeprime import homeprime
from homeprime.primality import is_prime

def main():
	# generate list of composite integers
	nmin = 4
	nmax = 111
	skip = [49, 77]
	n = []
	hp = []
	for k in range(nmin, nmax + 1):
		if not (is_prime(k) or k in skip):
			p = homeprime(k, verbose=True)
			n.append(k)
			hp.append(p)

	# compute logarithms
	log_hp = []
	loglog_hp = []
	for p in hp:

		d = len(str(p)) # number of digits
		x = d + np.log10(p / 10 ** d)
		log_hp.append(x)

		y = np.ceil(x)
		d = len(str(y))
		y = d + np.log10(x / 10 ** d)
		loglog_hp.append(y)

	## log scale ##

	# scatter plot: log scale
	plt.figure()
	plt.plot(n, log_hp, 'ko')
	plt.grid('on')
	plt.xlabel('$n$')
	plt.ylabel('$\log$HP$(n)$')
	plt.title('Home Prime Distribution')

	# histogram: log
	plt.figure()
	plt.hist(log_hp, bins=8)
	plt.xlabel('$\log$HP$(n)$')
	plt.ylabel('count')
	plt.title(f'Home Primes for {nmin}$\leq n\leq${nmax}')

	## double log scale ##

	# scatter plot: double log scale
	plt.figure()
	plt.plot(n, loglog_hp, 'ko')
	plt.grid('on')
	plt.xlabel('$n$')
	plt.ylabel('$\log\log$HP$(n)$')
	plt.title('Home Prime Distribution')

	# histogram
	plt.figure()
	plt.hist(loglog_hp, bins=8)
	plt.xlabel('$\log\log$HP$(n)$')
	plt.ylabel('count')
	plt.title(f'Home Primes for {nmin}$\leq n\leq${nmax}')

	# show all figures
	plt.show()

if __name__ == '__main__':
	main()