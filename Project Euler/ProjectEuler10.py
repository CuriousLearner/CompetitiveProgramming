#! /usr/bin/env python

'''
Project Euler 10 (https://projecteuler.net/problem=10)

Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

n = 2000000
sieve = [True] * n
def cross_out(sieve, i):
    for x in range(i + i, len(sieve), i):
        if sieve[x]:
            sieve[x] = False
for i in range(2, int(len(sieve) ** 0.5)):
    if sieve[i]:
        cross_out(sieve, i)
print(sum(i for i in range(2, len(sieve)) if sieve[i]))