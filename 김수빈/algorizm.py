#!/usr/bin/env python
# coding: utf-8

# In[1]:


#첫줄에 두정수 h와 m (0<=h<=23   0<=m<=59)
#24시간 표현
#45분 일찍

h,m=map(int,input().split()) 
#map는 여러 요소에 하나의 함수를 한꺼번에 대응시켜줄 수 있다
# 저장할 변수 = map(함수이름, 대응 요소)
#input().split() 함수의 실행 결과는 string 자료형의 두 숫자가 되기 때문에, 이를 int로 동시에 맵핑하기 위하여 map 함수를 적용.

m = m-45


if m<0:
    h = h-1
    m = m+60
    
if h<0:
    h = h+24
    
print(h,m)
    





