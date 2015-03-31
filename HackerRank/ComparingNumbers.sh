#!/bin/bash

# https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers

read num1
read num2
if [ $num1 -lt $num2 ]
then
echo "X is lesser than Y"
elif [ $num1 -gt $num2 ]
then
echo "X is greater than Y"
else
echo "X is equal to Y"
fi
