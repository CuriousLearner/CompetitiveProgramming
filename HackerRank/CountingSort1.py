#! /usr/bin/python3

# https://www.hackerrank.com/challenges/countingsort1

n = int(input())
ar = input()

count_dict = {el:0 for el in range(100)}
arr = ar.split(' ')

for item in arr:
    count_dict[int(item)] += 1

for value in count_dict.values():
    print(value, end=' ')
