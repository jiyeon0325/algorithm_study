from collections import deque

node, edge ,st = map(int, input().split()) #노드, 엣지, 시작점
graph = [[] for i in range(node + 1)] #각 위치마다 연결된 노드 저장
for i in range(edge):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited_dfs = [False] * (node+1) #bfs용 visit
visited_bfs = [False] * (node+1) #dfs용 visit
dfs_lst = []
bfs_lst = []
def dfs(graph, start, visited):
    visited[start] = True #첫 방문 노드 방문처리
    dfs_lst.append(start) #결과용 리스트에 append
    for i in graph[start]: #방문 노드 연결 노드 탐색
        if not visited[i]: #방문하지 않았다면
            dfs(graph, i, visited) #dfs 함수 재귀 실행

def bfs(graph, start, visited):
    queue = deque([start]) #첫 방문 노드 처음 덱에 투입
    visited[start] = True #처음 방문 노드 방문 처리
    while queue:
        v = queue.popleft() #맨 앞 노드 뽑아서
        bfs_lst.append(v)
        for i in graph[v]: #v과 연결된 노드 탐색
            if not visited[i]: #방문이 안됐다면
                queue.append(i) #큐에 넣기
                visited[i] = True #방문 처리, 처음으로 돌아가 반복



dfs(graph, st, visited_dfs)
bfs(graph, st, visited_bfs)
for i in dfs_lst:
    print(i, end = ' ')
print()
for i in bfs_lst:
    print(i, end = ' ')
