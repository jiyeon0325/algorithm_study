# def atm(a, b):
#     res = 0
#     for i in range(a+1):
#         res += b[i]
#     return res
#
# n = int(input())
# lst = list(map(int, input().split())) 처음 생각해본건데 x

n = int(input())
lst = list(map(int,input().split()))
lst.sort() # 먼저 정렬
sum = 0 # 합 정의
pd = n #곱하는 수 정의
for i in lst:
    sum += i * pd #첫 수는 n번 더해지고 그 다음수는 n-1 ...
    pd -= 1 # -1을 해준다 자동으로 1까지만 적용
print(sum)