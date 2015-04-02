#! /usr/bin/env python

# https://www.hackerrank.com/challenges/solve-me-second

def solveMeSecond(a,b):
   return a+b
n = int(input())
for i in range(0,n):
    a, b = input().split()
    a, b = int(a),int(b)
    res = solveMeSecond(a,b)
    print (res)
