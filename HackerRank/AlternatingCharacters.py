#! /usr/bin/env python

# https://www.hackerrank.com/challenges/alternating-characters

t = int(input())
for _ in range(t):
    chars = input()
    first_char = chars[0]
    deletion = 0
    for i in range(1, len(chars)):
        if chars[i] == first_char:
            deletion += 1
        else:
            first_char = chars[i]
    print(deletion) 
