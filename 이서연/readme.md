BOJ 단계별로 풀어보기
번호	문제	체크	level	분류
1	18870 좌표압축	✅	S2	정렬
2	1260 DFS와 BFS	⬜	S2	DFS/BFS
3	7576 토마토	⬜	G5	DFS/BFS
4	7569 토마토2	⬜	G5	DFS/BFS
5				

N = int(input("Input N: "))
nums= input("Input numbers: ").split()
N_list=list(map(int, nums))

N_list_sorted=sorted(N_list, reverse=True)
answer=[]
for i in N_list:
  index=N_list_sorted.index(i)
  count=len(N_list_sorted[i:])-1
  if i in N_list_sorted[index+1:]:
    count-=1
  answer.append(count)
print(*answer)
