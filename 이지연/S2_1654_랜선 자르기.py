# Parametric Search

# k: 이미 가지고 있는 랜선의 수
# n: 필요한 랜선의 수
# k개의 랜선을 잘라 n개의 같은 길이의 랜선으로 만들기
# 만들 수 있는 최대 랜선의 길이 구하기


k, n = map(int, input().split())
lan_list =[]
for _ in range(k):
    lan_list.append(int(input()))

# print(lan_list)

left = 1  # 자를 수 있는 가장 작은 길이
right = max(lan_list)   # 자를 수 있는 가장 긴 길이


# binary search
while left <= right:
    mid = (left + right) // 2
    
    cnt = 0 # 잘린 랜선 수
    for i in lan_list:
        cnt += i//mid
    
    # target 보다 개수가 작은 경우 
    if cnt < n:
        right = mid - 1   # 자를 수 있는 길이를 줄이기 위해 최대 길이를 줄임
    else:
        left = mid + 1

print(right)