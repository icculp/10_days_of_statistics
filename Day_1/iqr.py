#!/usr/bin/env python3
"""
    Day 0, challenge 2/2
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

inp = sys.stdin
lines = inp.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')
    lines[i] = lines[i].split(' ')
    for li in range(len(lines[i])):
        lines[i][li] = eval(lines[i][li])


length = lines[0][0]

num1 = lines[1]
num2 = lines[2]

'''
num1 = [10, 40, 30, 50, 20]
num2 = [1, 2, 3, 4, 5]
'''
'''
num1 = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20]
num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
nums = []
for i in range(len(num1)):
    for j in range(num2[i]):
        nums.append(num1[i])
'''print(nums)'''

'''nums = [4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12]'''
nums.sort()
length = len(nums)

med_i = int(length / 2)
lower = nums[0:med_i]
if length % 2 == 1:
    '''print('here')'''
    median = nums[med_i]
    upper = nums[med_i + 1:]
    q = int(len(lower) / 2)
    if q % 2 == 1:
        q1 = round(((lower[int(len(lower) / 2) - 1] + lower[int(len(lower) / 2)]) / 2), 1)
        q3 = round(((upper[int(len(upper) / 2)] + upper[int(len(upper) / 2)]) / 2), 1)
    else:
        q1 = round(lower[int(len(lower) / 2)], 1)
        q3 = round(upper[int(len(upper) / 2)], 1)
    '''print(q3)'''
else:
    median = (nums[med_i] + nums[med_i - 1]) / 2
    upper = nums[med_i:]
    q = int(len(lower) / 2)
    if q % 2 == 1:
        q1 = round(((lower[int(len(lower) / 2) - 1] + lower[int(len(lower) / 2)]) / 2), 1)
        q3 = round(((upper[int(len(upper) / 2) - 1] + upper[int(len(upper) / 2)]) / 2), 1)
    else:
        q1 = round(lower[int(len(lower) / 2)], 1)
        q3 = round(upper[int(len(upper) / 2)], 1)
lower = nums[0:med_i]

'''
print(q3)
print(q1)'''
print(round(float((q3 - q1)), 1))

