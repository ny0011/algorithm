from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10001)

def bfs(adj, node, visited, weight, answer):
    q = deque([node])
    visited[node] = True
    count = weight.pop(node)
    while q:
        current_node = q.popleft()
        for _node in adj[current_node]:
            if not visited[_node]:
                q.append(_node)
                visited[_node] = True
                count += weight.pop(_node)
    answer.append(count)

def dfs(adj, node, visited, weight, answer, i):
    stack = [node]
    visited[node] = True
    answer[i].append(weight.pop(node))
    for current_node in adj[node]:
        if not visited[current_node]:
            dfs(adj, current_node, visited, weight, answer, i)
            


def create_adj(maps):  
    adj = defaultdict(list)
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X":
                for k in range(len(dx)):
                    if i+dx[k] >= 0 and j+dy[k] >=0 and i+dx[k] < len(maps) and j+dy[k] < len(maps[0]) :
                        if maps[i+dx[k]][j+dy[k]] != "X" :
                            adj[(i,j)].append((i+dx[k],j+dy[k]))
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
    visited = dict()
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            visited[(i,j)] = False
    adj = create_adj(maps)
    weight = create_weight(maps)
    if len(weight) == 0:
        return [-1]
    
    i = 0
    while weight:
        node = list(weight.keys())[0]
        answer.append([])
        #bfs(adj, node, visited, weight, answer)
        dfs(adj, node, visited, weight, answer, i)
        i+= 1
    ret = []
    for _list in answer:
        ret.append(sum(_list))
    return sorted(ret)

solution(["X591X","X1X5X","X231X", "1XXX1"])
