# 입력 : [2, 4, -10, 4, -9]
# 출력 : [2, 3, 0, 3, 1]    i보다 작은 수 개수
# 정렬 : [-10, -9, 2, 4, 4]
# 집합 : {-10, -9, 2, 4}    idx 값과 같다
# dic  : {-10:0, -9:1, 2:2, 4:3} 

n = int(input())
li = list(map(int, input().split()))    # [2, 4, -10, 4, -9]
# li.sort()                             # 정렬 먼저하면 안된다.
# print(li)
# Set= set(li)
# print(Set)                            # 정렬 후 집합으로 만들면 {2, 4, -10, -9} 으로 출력됨
sorted_li= sorted(list(set(li)))        # 집합으로 만들고 리스트 만든 후 정렬 
# print(sorted_li)                        # [-10, -9, 2, 4]

dic = {}
for i in range(len(sorted_li)):
    dic[sorted_li[i]] = i

# print(dic)

for i in li:
    print(dic[i], end=' ')
