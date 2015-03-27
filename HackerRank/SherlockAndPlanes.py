#! /usr/bin/env python

# https://www.hackerrank.com/challenges/sherlock-and-planes

t = int(input())
for _ in range(t):
    x1, y1, z1 = input().split()
    x2, y2, z2 = input().split()
    x3, y3, z3 = input().split()
    x4, y4, z4 = input().split()
    x1, y1, z1 = int(x1), int(y1), int(z1)
    x2, y2, z2 = int(x2), int(y2), int(z2)
    x3, y3, z3 = int(x3), int(y3), int(z3)
    x4, y4, z4 = int(x4), int(y4), int(z4)
    if (x1 == x2 == x3 == x4) or (y1 == y2 == y3 == y4) or (z1 == z2 == z3 == z4):
        print("YES")
    else:
        print("NO")
