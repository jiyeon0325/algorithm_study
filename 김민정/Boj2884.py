#!/usr/bin/env python
# coding: utf-8

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

