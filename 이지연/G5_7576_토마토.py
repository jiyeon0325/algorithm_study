# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
# 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.(하루)
# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토
# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하기
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 
# 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
# 6 4
# 1 -1 0 0 0 0
# 0 -1 0 0 0 0
# 0 0 0 0 -1 0
# 0 0 0 0 -1 1

# 1 -1 7 6 5 4
# 2 -1 6 5 4 3
# 3  4 5 6 -1 2
# 4  5 6 7 -1 1

# 0이 없어질 때까지 bfs
# 걸린 날짜는 7보다 1 작은 6일

from collections import deque

# 열, 행의 개수
m, n = map(int, input().split())

# 지도 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)

# 방문 정보 저장
visited = [[0]*m for _ in range(n)]

# 4방 이동(상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# bfs 구현을 위한 큐
q = deque([])

# bfs
def bfs(r, c):

    while q:
        r, c = q.popleft()

        # 현재 정점에서 4방 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 지도를 벗어나는 경우
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            # 이미 방문한 경우
            if graph[nr][nc] == 1:
                continue

            # 토마토가 없는 위치인 경우
            if graph[nr][nc] == -1:
                continue
            
            # 4방 탐색 중 모든 조건을 만족하는 경우
            if visited[nr][nc] == 0 and graph[nr][nc] == 0:
                graph[nr][nc] = graph[r][c] + 1
                q.append([nr, nc])
                visited[nr][nc] = 1

# main
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:       # 익은 토마토의 위치
            q.append([i, j])       # 큐에 넣고
            visited[i][j] = 1      # 방문 처리

bfs(i, j)     # bfs 실행

zero_flag = False   # 익지 않은 토마토 flag 
max_day = 0       # 토마토가 모두 익는데 걸린 최대 기간

# 토마토가 모두 익는데 걸린 최대 기간 구하기
# 예외 처리 (토마토가 모두 익지 못하는 상황이면 -1을 출력)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:    # 익지 않은 토마토가 존재하는 경우
            zero_flat = True
        max_day = max(max_day, graph[i][j])

if zero_flag == True:
    print(-1)
else:
    print(max_day -1)
