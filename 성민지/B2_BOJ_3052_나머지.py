#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# boj 3052

nums = {}

for _ in range(10) :
    num = int(input())
    ans = num % 42
    
    if ans in nums.keys() :
        nums[ans] += 1
    else :
        nums[ans] = 1

print(len(nums.keys()))

