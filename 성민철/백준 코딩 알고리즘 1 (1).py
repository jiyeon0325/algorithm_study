#!/usr/bin/env python
# coding: utf-8

# In[11]:


#첫째 줄 
#둘째 줄 공백 한 칸
#여기서 리스트 내부에서 크기를 비교해야하는데 그 부분에서 막혔음

a = 5
b = [2, 4, -10, 4, -9]
c = 0
f = 0
d = []
for i in range(len(b)):
    for e in b:
        if b[i] > e:
            c += 1
    d.append(c)
    c = 0 

print(d)
        


# In[13]:


a = 6
b = [1000, 999, 1000, 999, 1000, 999]
c =0
f = 0
d =[]
for i in range(len(b)):
    for e in b:
        if b[i] > e:
            c += 1
    d.append(c)
    c = 0 

print(d)


# In[ ]:




