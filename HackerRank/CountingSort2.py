#! /usr/bin/python3

# https://www.hackerrank.com/challenges/countingsort2

n = int(input())
ar = input()

arr = ar.split(' ')

arr.sort(key = int)
for item in arr:
    print(item, end = ' ')
