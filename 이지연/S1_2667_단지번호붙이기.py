# 1은 집이 있는 곳을, 0은 집이 없는 곳
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력

# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 0110200
# 0110202
# 1110202
# 0000222
# 0300000
# 0333330
# 0333000

# 단지 번호로 모두 표기 후 각 단지 번호를 가지는 집의 수 구하여 정렬

# 지도 크기
n = int(input())

# 지도 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# print(graph)

# 방문 정보 저장
visited = [[0]*n for _ in range(n)]

# 4방 이동(상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 단지 번호
index = 1
# 단지 내 집의 수 리스트
home_list = [] 
# 단지 내 집의 수
home_cnt = 0

# dfs
def dfs(r, c, i):
    visited[r][c] = 1        # 현재 정점 방문 처리    
    global home_cnt      

    if graph[r][c] == 1:     # 현재 정점에 집이 있으면
        home_cnt += 1        # 집의 수 1 증가
        graph[r][c] = i      # 단지번호(index)로 인덱싱

    # 현재 정점에서 4방 탐색
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 지도를 벗어나는 경우
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue

        # 이미 방문한 경우
        if visited[nr][nc] == 1:
            continue

        # 집의 위치가 아닌 경우
        if graph[nr][nc] == 0:
            continue

        # 4방 탐색 중 모든 조건을 만족하는 경우
        if visited[nr][nc] == 0 and graph[nr][nc] == 1:
            dfs(nr, nc, i)
        
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j, index)
            home_list.append(home_cnt)
            home_cnt = 0   # 다시 초기화
            index += 1     

print(index-1)
for cnt in sorted(home_list):
    print(cnt)

