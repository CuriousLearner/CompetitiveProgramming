#! /usr/bin/env python

# https://www.hackerrank.com/challenges/handshake

def cal(n):
    res = 0
    for i in range(n):
        res += i
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    print(cal(n)) 
