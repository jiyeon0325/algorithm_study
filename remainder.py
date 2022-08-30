#!/usr/bin/env python
# coding: utf-8

# In[3]:


remainder = []


for i in range(10):
    in_num = int(input())
    remainder.append(in_num % 42)
    
    
    
result = []


for i in remainder:
    if i not in result:
        result.append(i)
    
    
print(len(result))


# In[ ]:




