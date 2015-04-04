#! /usr/bin/env python

# https://www.hackerrank.com/challenges/gem-stones

n = int(raw_input())
first_input = set(raw_input())

for i in range(n-1):
    rest_input = set(raw_input())
    first_input = first_input & rest_input

print(len(first_input))
