#! /usr/bin/env python

'''
Project Euler 6 (https://projecteuler.net/problem=6)

Sum Square Difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

def sum_of_squares(n):
    res = 0
    for i in range(1, n + 1):
       res += i ** 2
    return res

def square_of_sum(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res ** 2

print(square_of_sum(100) - sum_of_squares(100))
