#! /usr/bin/env python

'''
Project Euler 48 (https://projecteuler.net/problem=48)

Self Powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

'''

res = 0
for i in range(1, 1001):
    res += i ** i
print(str(res)[::-1][:10][::-1])
