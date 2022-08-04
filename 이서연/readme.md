
# BOJ 단계별로 풀어보기 
| 번호 | 문제 | 체크 | level |  
|:---:|:---|:---:|:---:|
| 1 | 2884 알람시계 | ✅ | B3 |
| 2 | 1110 더하기 사이클 | ⬜ | B1 |
| 3 | 4344 평균은 넘겠지 | ⬜ | B1 |
| 4 | 2577 숫자의 개수 | ⬜ | B2 | 
| 5 | 3052 나머지 | ⬜ | B2 |


N = int(input("Input N: "))
nums= input("Input numbers: ").split()
N_list=list(map(int, nums))

N_list_sorted=sorted(N_list, reverse=True)
# N_list_sorted
answer=[]
for i in N_list:
  index=N_list_sorted.index(i)
  count=len(N_list_sorted[i:])-1
  if i in N_list_sorted[index+1:]:
    count-=1
  answer.append(count)
print(*answer)
