#! /usr/bin/env python

# https://www.hackerrank.com/challenges/utopian-tree

t = int(input())
for _ in range(t):
    g = 1
    n = int(input())
    for i in range(0, n):
        if i % 2 == 0:
            g *= 2
        else:
            g += 1
    print(g)
