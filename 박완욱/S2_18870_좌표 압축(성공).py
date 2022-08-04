n = int(input())
lst = list(map(int, input().split()))
a = list(set(lst))
a.sort()

dic = {a[i] : i  for i in range(len(a))}


for i in lst:
    print(dic[i], end = ' ')