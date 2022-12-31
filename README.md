# homeprime

Version 0.1.1
-----------------
https://github.com/samreynoldsmath/homeprime

Description
-----------------
Tools for computing and testing conjectures about home primes.

Given an integer $n > 1$, consider the integer $m$ obtained by concatenating
the prime factors of $n$ (in ascending order, with repeats, and in base $10$).
Iterate this map until a prime number is obtained.
This prime number is called the **home prime** of $n$,
and is denoted by $\text{HP}(n)$.

**Example:** $99$ factors as $3 \cdot 3 \cdot 11$.
After concatenation, we factor $3311$ as $7 \cdot 11 \cdot 43$.
Concatenation gives $71143$, which is prime, so $\text{HP}(99) = 71143$.

The smallest natural number $n$ for which $\text{HP}(n)$ is unknown is
$n = 49$.

*World of Numbers* has a great article here:
http://www.worldofnumbers.com/topic1.htm

-----------------
Copyright (C) 2022 - 2023 Samuel E. Reynolds.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.