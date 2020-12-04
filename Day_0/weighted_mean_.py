#!/usr/bin/env python3
"""
    Day 0, challenge 2/2
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
import sys


s = sys.stdin.readlines()

length = eval(s[0].strip('\n'))

nums = s[1].split(' ')
nums = [eval(i) for i in nums]

weight = s[2].split(' ')
weight = [eval(i) for i in weight]

for i in range(length):
    nums[i] = nums[i] * weight[i]

ws = sum(weight)
    
mean = sum(nums) / sum(weight)
print(round(mean, 1))
