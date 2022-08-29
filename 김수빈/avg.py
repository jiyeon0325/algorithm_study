#!/usr/bin/env python
# coding: utf-8

# In[16]:


c = int(input())


for i in range(c):
    s = list(map(int, input().split()))
    mean = sum(s[1:])/s[0]
    count = 0
    
    for q in s[1:]:
        
        if q > mean:
            count += 1

            
    per = ((count / s[0])*100)
    print(f'{per:.3f}%')

