'''
기본 idea는 첫 - 에서 묶고, 그 다음 - 가 나오기 전까지 묶는 것
최대한 많은 수를 더해서 빼주어야 함.
'''

a = input().split('-') #-를 기준으로 나눔
for i in a:
    cnt = 0 #숫자 저장 변수
    s = i.split('+') #+ 기준으로 나누고
    for j in s:
        cnt += int(j) # + 기준으로 나눈 리스트에서 모든 원소 더하기
    num.append(cnt) #더한 수 넣기

n = num[0] #연산을 시작하는 수 지정
for i in range(1, len(num)):
    n -= num[i] # + 만 있다면 n만 출력될것임.
print(n)