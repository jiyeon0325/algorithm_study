# 높이 h 이상 부분이 모두 잘림
# 잘린 부분만 집에 가져감
# n: 나무의 수, m: 집으로 가져가려고 하는 나무 길이
# 적어도 m미터 나무를 집에 가져가기 위한 높이 h의 최댓값 출력

n, m = map(int, input().split())
tree_list = list(map(int, input().split()))  # 나무 높이

# h의 최소, 최대
left = 1
right = max(tree_list)

while left <= right:
    mid = (left+right)//2
    
    tree_len = 0              # 잘린 나무의 길이
    for i in tree_list:
        if i > mid:           # mid보다 큰 나무만 잘림
            tree_len += i - mid
    
    # target 보다 작은 경우 (m보다 더 많이 가져가야함)
    if tree_len < m:
        right = mid - 1  # 자를 수 있는 높이를 줄이기
    else:
        left = mid + 1
   
print(right)