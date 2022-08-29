n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
count = [] #아파트 갯수 확인하는 용도
cnt = 0 #아파트 마다 단지 수 세기
dx = [0,0,1,-1] #이동 단위 리스트
dy = [1,-1,0,0] #이동 단위 리스트

def dfs(x, y): #x는 x쪽 방향, y는 y쪽 방향
    global cnt #전역 변수 지정
    # if x <= -1 or x >= n or y <= -1 or y >= n:
    #     return False 왜 안될까????
    if graph[x][y] == 1:
        graph[x][y] = 0 #0으로 방문 여부 표시
        cnt += 1 #세대수 카운트
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n: #만약 nx와 ny가 범위 안에 있다면 dfs함수 실행
                dfs(nx, ny)
    else:
        return False #0이면 멈추기, return False
    # else:
    #     graph[x][y] = 0
    #     cnt += 1
    #     dfs(x - 1,y)
    #     dfs(x, y - 1)
    #     dfs(x + 1, y)
    #     dfs(x, y + 1)
    #     return True




for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            count.append(cnt)


print(len(count))
for i in count:
    print(i, end = '\n')
