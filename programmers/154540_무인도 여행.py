from collections import deque

def bfs(adj, node, visited, weight, answer):
    a, b = node
    q = deque([node])
    visited[a][b] = True
    count = weight.pop((a,b))
    while q:
        x, y = q.popleft()
        for i, j in adj[x][y]:
            if not visited[i][j]:
                q.append((i,j))
                visited[i][j] = True
                count += weight.pop((i,j))
    answer.append(count)

def create_adj(maps):  
    adj = [[[] for j in range(len(maps[0]))] for i in range(len(maps))]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X":
                for k in range(len(dx)):
                    if i+dx[k] >= 0 and j+dy[k] >=0 and i+dx[k] < len(maps) and j+dy[k] < len(maps[0]) :
                        if maps[i+dx[k]][j+dy[k]] != "X" :
                            adj[i][j].append((i+dx[k],j+dy[k]))
    return adj

def create_weight(maps):
    weight = dict()
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X":                
                weight[(i,j)] = int(maps[i][j])
    return weight

def solution(maps):
    answer = []
    visited = [ [False for j in range(len(maps[0]))] for i in range(len(maps)) ]
    adj = create_adj(maps)
    weight = create_weight(maps)
    if len(weight) == 0:
        return [-1]
    
    while weight:
        node = list(weight.keys())[0]
        bfs(adj, node, visited, weight, answer)
    
    return sorted(answer)
