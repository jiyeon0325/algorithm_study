#!/usr/bin/env python
# coding: utf-8

# In[4]:


time = map(int,input().split())
h, m = time

if m < 45:
    if h == 0:
        h = 23
        m += 60
    else:
        h -= 1
        m += 60
print(h,m-45)
        


# In[ ]:




