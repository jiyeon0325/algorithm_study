# 26 -> 2+6=8 -> 68 -> 6+8=14 -> 84 -> 8+4=12 -> 42 -> 4+2=6 -> 26

n = int(input())   # 26
origin = n

cnt = 0 # 사이클 길이

while True:
    n = (n // 10 + n % 10) % 10 + (n % 10) * 10  # 68
    cnt += 1

    if n == origin:
        break

print(cnt)