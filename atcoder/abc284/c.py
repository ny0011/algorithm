from collections import deque

def bfs(g, visited, v):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        for i in g[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True



N, M = map(int, input().split())
g = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    

visited = [False] * (N+1)
count = 0

for v in range(1, N+1):
    if visited[v]: 
        continue
    bfs(g,visited,v)
    count +=1

print(count)
    
