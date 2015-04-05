#! /usr/bin/python3

# https://www.hackerrank.com/challenges/pangrams

import string

line = set(input().lower())
setofalpha = set(string.ascii_lowercase)
result = setofalpha - line
if result:
    print("not pangram")
else:
    print("pangram")
