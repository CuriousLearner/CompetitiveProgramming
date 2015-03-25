#! /usr/bin/env python

# https://www.hackerrank.com/challenges/connecting-towns

t = int(input())
for _ in range(t):
    n = int(input())
    r = input()
    routes = [int(i) for i in r.split()]
    res = 1
    for i in routes:
        res *= i
    print(res % 1234567)
