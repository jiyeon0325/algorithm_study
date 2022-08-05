# 55 185   rank 2  
# 58 183           rank 2
# 88 186                   rank 1
# 60 175                           rank 2
# 46 155                                   rank 5

n = int(input())

people = []
for _ in range(n):
    w, h = map(int, input().split())
    people.append((w, h))

for i in people:
    rank = 1             # i번 째 사람 rank

    for j in people:
        if (i[0] != j[0]) and (i[1] != j[1]):
            if (i[0] < j[0]) and (i[1] < j[1]):
                rank += 1

    print(rank)          # i번 째 사람 rank 출력

