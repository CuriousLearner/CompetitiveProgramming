#! /usr/bin/env python

# https://www.hackerrank.com/challenges/find-point

t = int(input())
for _ in range(t):
    px, py, qx, qy = input().split()
    px, py, qx, qy = int(px), int(py), int(qx), int(qy)
    rx = 2 * qx - px
    ry = 2 * qy - py
    print(rx, ry)
