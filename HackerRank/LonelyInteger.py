#! /usr/bin/env python

# https://www.hackerrank.com/challenges/lonely-integer

from itertools import groupby
n = int(input())
mylist = input()
a = [int(i) for i in mylist.split()]
for key, group in groupby(sorted(a)):
    if len(list(group)) == 1:
        print(key)
