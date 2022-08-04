n = int(input())
lst = list(map(int, input().split()))
idx = [i for i in range(len(lst))]
for i in range(n):
    cnt = 0
    for j in range(n):
        if lst[i] > lst[j]:
            cnt += 1
    idx[i] = cnt
print(idx)