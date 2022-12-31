"""
Example 2

The home prime of 80 is
HP(80) = 313169138727147145210044974146858220729781791489
in 31 steps
"""

from homeprime.homeprime import homeprime
from time import time

def main():
	n = 80
	t = time()
	homeprime(n, verbose=True)
	t = time() - t
	print('Elapsed time: %.4g seconds'%(t))

if __name__ == '__main__':
	main()