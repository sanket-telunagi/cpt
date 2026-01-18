# Solution for primes
# Platform: utils
# Date: 2026-01-18
#

import random
import math


def is_prime(n):
    """Deterministic Miller-Rabin for n < 2^64."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Bases for deterministic Miller-Rabin up to 2^64
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Specific bases needed to guarantee 100% accuracy for 64-bit integers
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n <= a:
            break
        if not miller_test(n, a, d, s):
            return False
    return True


def miller_test(n, a, d, s):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False


def get_single_factor(n):
    """Pollard's Rho algorithm to find a single non-trivial factor."""
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if is_prime(n):
        return n

    while True:
        c = random.randint(1, n - 1)
        x = random.randint(2, n - 1)
        y = x
        g = 1
        while g == 1:
            # f(x) = (x^2 + c) % n
            x = (pow(x, 2, n) + c) % n
            # y = f(f(y))
            y = (pow(y, 2, n) + c) % n
            y = (pow(y, 2, n) + c) % n
            g = math.gcd(abs(x - y), n)

        # If g == n, the cycle failed to find a factor, retry with different c
        if g != n:
            return g


def factorize(n):
    """Recursive function to find all prime factors and return a sorted list."""
    if n == 1:
        return []
    if is_prime(n):
        return [n]

    factors = []
    # Find one factor
    d = get_single_factor(n)
    # Recursively factorize the results
    factors.extend(factorize(d))
    factors.extend(factorize(n // d))
    return sorted(factors)


def count_factors_by_dict(n):
    freq = {}

    factors = factorize(n)

    for num in factors:
        if freq.get(num, None):
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


def get_distinct_prime_factors_by_pollard_method(n):
    if n == 1:
        return set()
    if is_prime(n):
        return {n}  # Use the Miller-Rabin test from previous answer

    factors = set()
    temp = n

    def find_factors(num):
        if num == 1:
            return
        if is_prime(num):
            factors.add(num)
            return

        # Pollard's Rho logic to find one factor
        d = get_single_factor(num)  # Use the Rho function from previous answer

        # Once we find a factor 'd', find all prime factors of 'd'
        # and then factorize what's left of 'num'
        find_factors(d)
        find_factors(num // d)

    find_factors(n)
    return sorted(list(factors))
