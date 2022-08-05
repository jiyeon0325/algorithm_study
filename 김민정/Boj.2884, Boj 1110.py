#!/usr/bin/env python
# coding: utf-8

# ## Boj 2884

# In[1]:


## 45분 앞서는 시간으로 바꾸는 것
#0<=H<=23, 0<=M<=59, H시M분, 24시간 표현 0:0~23:59
#1st - M-45
#if M-45>0 = H시 M-45분
#elif M-45<0, H>0 = H-1시 (60+M)-45분
#근데 H-1이 0이면
#(ex) 0시 30분 => -1시 45분 --> 23시 45분 (H-1)+24를 해줘야함  -> H == 0 -> H = 23
#(ex2) 1시 30분 => 0시 45분 


# In[41]:


H = int(input('시간입력: '))
M = int(input('분입력: '))
print(type(H))
print(type(M))


# In[42]:


if M-45>=0:
    print(H,M-45)
elif M-45<0:
    M = M+60
    if H-1 < 0:
        New_H = (H-1)+24
        print(New_H,M-45)


# In[44]:


H = int(input('시간입력: '))
M = int(input('분입력: '))

if M-45>=0:
    print(H,M-45)
elif M-45<0:
    M += 60
    print(H,M-45)
    if H == 0:
        H+=23
        print(H,M-45)


# In[50]:


H = int(input('시간입력: '))
M = int(input('분입력: '))

if H == 0:
    H+=23
elif M-45>=0:
    H=H
    M-=45
else:
    H-=1
    M+=60-45
print(H,M)


# In[10]:


H, M = map(int,input('시와 분을 입력하세요: ').split())
        
if H!=0:
    if M-45>=0:
        H = H
        M-= 45
    else:
        H-=1
        M+=60-45
else:
    H=24
    if M-45>=0:
        H+=23
        M-=45
    else:
        H-=1
        M+=60-45
print(H,M)


# In[18]:


H, M = map(int,input('시와 분을 입력하세요: ').split())

if M-45<0:
    if H == 0:
        H = 23
        M += 60
    else:
        H-=1
        M += 60
else:
    
print(H,M-45)


# In[ ]:


H, M = map(int,input().split()) 
#한줄에 변수를 받아야함
#H,M을 input하여 공백 기준으로 split >> map 사용하여 int로 타입 변경 

if M-45>=0:
    print(H,M-45)
#분이 45분보다 클 경우 별도의 추가작업 필요 없으므로 해당 시간과 M-45 출력
elif H>0 and M-45<0:
    M+=60
    print(H-1,M-45)
#시간이 0보다 크고 분이 45분보다 작을 경우
#분을 양수로 출력해야하므로 해당 시간-1과 M+60-45 출력
else:
    M+=60
    print(H+23,M-45)
#시간이 0인 경우 (?) 현재시간+23과 M-45 출력 


# ## Boj 1110

# In[1]:


#0<=X<=99
#IF X<10 = 0X
#NEXT 0+X 
#NEXT 0X(0+X) >> X(0+X)의 뒷자리 = 새로운 변수 (A)
#for i 
#IF X == A: break 
#or continue => 반복 
#ELSE X=CD(두자리수 가정)
#C+D = EF
#DF
#IF CD == DF: break or contiunue


# In[14]:


N = int(input())
SUM_N = (N//10) + (N%10)
k = 0
while True:
    elif SUM_N <10:
        SUM_N = (N%10)*10 + SUM_N
    else:
        SUM_N = (N%10)*10 + (SUM_N%10)
        if SUM_N == N:
            k+=1
            break
            print(k)


# In[28]:


N = int(input())
#int형 변수 N 출력

original_number = N
#처음 입력했던 N값을 기억해야하므로 새변수 orginial_number를 만들어 현재 N 저장
sum_number = 0
#더하기 연산 처리를 위해 sum_number라는 새변수 선언
new_number = 0
#상단 연산 이후 생성된 새로운 숫자를 받기위해 new_number라는 새변수 선언
k = 0
#사이클 수 카운팅을 위해 k라는 새변수 선언
while True:
#while True = 항상 참이므로 무한루프 생성 
    sum_number = (N//10) + (N%10)
#각 자리의 숫자를 더하는 연산 = int 변수의 몫 + int 변수의 나머지
    new_number = (N%10)*10 + (sum_number%10)
# 상단 연산 후 생긴 숫자의 가장 오른쪽 자리수와 주어진 수의 가장 오른쪽 자리 이어붙이기
# (int 변수의 나머지)*10 (10의자리수로 변환) + 더하기 연산값의 나머지 (1의자리수로 변환)
    k+=1
#사이클 수 카운팅 (?)
    N = new_number
#새롭게 생성된 숫자를 int형 변수에 입력 (무한루프를 위해)
    if new_number == original_number:
        break
print(k)
#새로운 숫자와 처음 입력한 N값이 같을때의 k(사이클수) 출력


# In[ ]:




