#! /usr/bin/env python

# https://www.hackerrank.com/challenges/maximizing-xor

l = int(input())
r = int(input())
max_xor = 0
for i in range(l, r + 1):
    for j in range(l, r + 1):
        xor = i ^ j
        if xor > max_xor:
            max_xor = xor
print(max_xor)
