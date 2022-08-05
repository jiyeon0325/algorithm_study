#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

