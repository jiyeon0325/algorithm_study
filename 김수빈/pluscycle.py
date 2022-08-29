#!/usr/bin/env python
# coding: utf-8

# In[2]:


number = int(input())
num = number
count = 0


while 1:
    sum_ = (num//10) + (num%10)
    new_num = ((num%10)*10) + (sum_%10)
    count += 1
    
    if new_num == number:
        break
        
    num = new_num
    
print(count)


# In[ ]:




