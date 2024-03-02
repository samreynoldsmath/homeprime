"""
Example 0

Factoring a large integer
"""

from homeprime.factor import factor


def main():
    n = 123456789
    f = factor(n)
    print(f)


if __name__ == "__main__":
    main()
