#!/usr/bin/env python3
"""
    Day 0, challenge 2/2
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import pstdev
import sys

inp = sys.stdin
inp = inp.readlines()
nums = inp[1].split(' ')
for i in range(len(nums)):
    nums[i] = eval(nums[i])
print(round(pstdev(nums), 1))


