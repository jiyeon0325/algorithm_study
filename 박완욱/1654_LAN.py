N, K = map(int, input().split())
lan = []
for i in range(N):
    n = int(input())
    lan.append(n)

start = 1 #시작점 설정
end = max(lan) #종료점 설정
while (start <= end): #start가 end보다 크면 종료
    mid = (start + end) // 2 #가운데값 설정
    cnt = 0 #랜 갯수 세는 것
    for i in lan:
        cnt += i // mid
    if cnt >= K: #랜 갯수가 K개보다 많다면
        start = mid + 1 #end와 가까워지도록 mid + 1 더하기
        # break
    elif cnt < K: #랜 갯수가 적다면
        end = mid - 1 # end를 mid - 1로 재설정

print(end)
