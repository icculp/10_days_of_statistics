#!/usr/bin/env python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
import sys
from scipy import stats


s = sys.stdin.readlines()

l = eval(s[0].strip('\n'))

nums = s[1].split(' ')
nums = [eval(i) for i in nums]

mean = statistics.mean(nums)
print(round(mean, 1))
median = statistics.median(nums)
print(round(median, 1))
mode = stats.mode(nums)
'''except statistics.StatisticsError:
    mode = statistics.multimode(nums)
    mode = min(mode)'''
print(min(mode.mode))

