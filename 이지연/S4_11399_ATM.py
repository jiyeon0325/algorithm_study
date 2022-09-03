# n: 줄 서 있는 사람의 수, p: 각 사람이 돈을 인출하는 데 걸리는 시간
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값 구하기

n = int(input())
p_list = list(map(int, input().split()))

p_list.sort()
# print(p_list)

time_list=[]
time = 0
for i in p_list:
    time += i
    time_list.append(time)

# print(time_list)
print(sum(time_list))