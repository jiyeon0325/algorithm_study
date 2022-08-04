# 처음
n = input()
n.sort(reverse = t=True)
for i in n:
    print(i,end="")

# for 문에서 문자열을 list처럼 한 문자열씩 받아서 넘길 수 있길래 list와 비슷하다고 생각하고 풀음
# 결과 실패







# 마지막 수정본
a = input()
n = []
for i in a:
    n.append(i)
n.sort(reverse = True)

for j in n:
    print(j, end="")
    
# for 문을 돌려 문자열의 각각의 원소를 받아서 넘김
