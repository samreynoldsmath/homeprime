from .factor import factor

def homeprime(n: int, depth: int='inf', verbose: bool=False):
	"""
	Returns the home prime of n.

	Set maximum number of function compositions to m with depth=m.

	Set verbose=True to get terminal output.
	"""
	if depth == 'inf':
		depth = float('inf')
	is_prime = False

	# optional print to terminal
	if verbose:
		print(60 * '-')
		print(f'0:\t', [n])

	# depth counter
	d = 0

	while not is_prime and d < depth:
		d += 1

		# obtain the prime factorization
		f = factor(n)

		# safety check to ensure calculation succeeded
		if not f.success:
			print(f)
			raise Exception('Factorization of {f.n} failed')

		# concatenate the digits
		m = ''
		for p in f.factors:
			m += str(p)
		n = int(m)

		# check if prime
		is_prime = f.num_factors == 1

		# optional print to terminal
		if verbose:
			print(f'{d}:\t', f.factors)

		# premature termination message
		if d == depth and not is_prime:
			msg = f'Maximum depth of {depth} reached'
			msg += f' without finding home prime'
			print(msg)

	# assuming there is only one factor to be returned
	return f.factors[0]
