#!/usr/bin/env python
# coding: utf-8

# In[11]:


#첫째 줄 
#둘째 줄 공백 한 칸


a = 5			#N정의
b = [2, 4, -10, 4, -9]  #N1, N2, N3...를 리스트로 정리하기
c = 0			
f = 0
d = []			#빈 리스트 지정 
for i in range(len(b)): #for문 사용하기, i는 리스트의 성질 활용하기 위해서 배정 
    for e in b:		#리스트에서 값 꺼내기
        if b[i] > e:	#비교하기 
            c += 1	#조건 만족할 때마다 하나씩 더하기
    d.append(c)		#리스트에 추가
    c = 0 		#초기화

print(d)
        


# In[13]:


a = 6					#N정의
b = [1000, 999, 1000, 999, 1000, 999]   #N1, N2, N3...를 리스트로 정리하기
c =0					#변수 지정 
f = 0					 
d =[]					#빈 리스트 지정
for i in range(len(b)):			#for문 사용하기, i는 리스트의 성질 활용하기 위해서 배정 
    for e in b:
        if b[i] > e:			#비교하기 
            c += 1			#조건 만족할 때마다 하나씩 더하기
	    break			#중복 방지			
    d.append(c)				#리스트에 추가 
    c = 0 				#초기화

print(d)


# In[ ]:




