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
nums = lines[1]
'''nums = [4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12]'''
nums.sort()
'''print(nums)'''

'''length = 12'''

lines = [3, 7, 8, 5, 12, 14, 21, 15, 18, 14]

med_i = int(length / 2)
lower = nums[0:med_i]
if length % 2 == 1:
    median = nums[med_i]
    upper = nums[med_i + 1:]
    q1 = int((lower[int(len(lower) / 2) - 1] + lower[int(len(lower) / 2)]) / 2)
    q3 = int((upper[int(len(upper) / 2) - 1] + upper[int(len(upper) / 2)]) / 2)
    '''print(q3)'''
else:
    median = (nums[med_i] + nums[med_i - 1]) / 2
    upper = nums[med_i:]
    q = int(len(lower) / 2)
    if q % 2 == 1:
        q1 = int((lower[int(len(lower) / 2) - 1] + lower[int(len(lower) / 2)]) / 2)
        q3 = int((upper[int(len(upper) / 2) - 1] + upper[int(len(upper) / 2)]) / 2)
    else:
        q1 = int(lower[int(len(lower) / 2)])
        q3 = int(upper[int(len(upper) / 2)])
lower = nums[0:med_i]




print(int(q1))
print(int(median))
print(int(q3))

