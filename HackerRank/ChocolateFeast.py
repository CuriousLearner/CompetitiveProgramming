#! /usr/bin/env python

# https://www.hackerrank.com/challenges/chocolate-feast

t = int(input())
for _ in range(t):
    n, c, m = input().split()
    n, c, m = int(n), int(c), int(m)
    total_choco = n // c
    wrappers = total_choco
    while wrappers >= m:
        total_choco += 1
        wrappers += 1
        wrappers -= m
    print(total_choco)
