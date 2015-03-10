#! /usr/bin/env python

'''
Project Euler 4 (https://projecteuler.net/problem=4)

Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 X 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def is_palindrome(n):
    return( str(n)[::-1] == str(n))

prod = []
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if is_palindrome(i * j):
            prod.append(i * j)

print(max(prod))
