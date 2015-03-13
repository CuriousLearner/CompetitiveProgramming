#! /usr/bin/env python

'''
Project Euler 16 (https://projecteuler.net/problem=16)

Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

'''

num = 2 ** 1000
def PowerDigitSum(num):
    numbers = [int(i) for i in str(num)]
    return sum(numbers)
print(PowerDigitSum(num))
