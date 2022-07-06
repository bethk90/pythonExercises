"""
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.
"""

def divisors(n):
    total = 0
    for x in range(1, n+1):
        if n % x == 0:
            total += 1
    return total