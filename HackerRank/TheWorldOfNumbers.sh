#!/bin/bash

# https://www.hackerrank.com/challenges/bash-tutorials---the-world-of-numbers

read num1
read num2
echo $[$num1+$num2]
echo $(($num1-$num2))
echo $[$num1*$num2]
echo $[$num1/$num2]
