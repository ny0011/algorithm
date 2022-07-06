import heapq

def prim(graph):
    n = len(graph)
    visited = [False]*n
    heap = []
    total = 0
    edge = 0 
    heapq.heappush(heap, (0, 0))
    while len(heap) > 0:
        if edge == n:
            break
        cost, vertex = heapq.heappop(heap)        
        if not visited[vertex]:
            edge +=1
            visited[vertex] = True
            total += cost
            for connected_cost, connected_vertex in graph[vertex]:
                heapq.heappush(heap, (connected_cost, connected_vertex))
    return total

def distance(a,b):
    return min(abs(a[0]-b[0]),abs(a[1]-b[1]),abs(a[2]-b[2]))   

def make_graph(vertexs,i,graph):
    ax,ay,az,j = vertexs[i]
    bx,by,bz,k = vertexs[i+1]
    cost = distance((ax,ay,az),(bx,by,bz))
    graph[j].append((cost, k))
    graph[k].append((cost, j))

def main():
    
    n = int(input())
    vertexs = list()
    for i in range(n):
        x,y,z=map(int, input().split(" "))
        vertexs.append((x,y,z,i))
    
    sorted_x = sorted(vertexs, key=lambda vertex: vertex[0] )
    sorted_y = sorted(vertexs, key=lambda vertex: vertex[1] )
    sorted_z = sorted(vertexs, key=lambda vertex: vertex[2] )
    
    graph=[[] for _ in range(n)]
    
    for i in range(n-1):
        make_graph(sorted_x,i,graph)
        make_graph(sorted_y,i,graph)
        make_graph(sorted_z,i,graph)    


    answer = prim(graph)
    print(answer) 
    
main()

'''
1. ---0.14122343063354492s seconds---
2. ---0.5858089923858643s seconds---
3. ---1.9207887649536133s seconds---
411620680
'''

'''
MAX = 2000000001
def calculate_cost(p1, p2):
    return min(abs(p1[0]-p2[0]),abs(p1[1]-p2[1]),abs(p1[2]-p2[2]))

def push_item(graph, start, end):
    if start not in graph:
        graph[start] = set([end])
    else:
        graph[start] = end

def main():
    n = int(input())
    arr = list()
    for _ in range(n):
        arr.append(list(map(int, input().split(" "))))

    answer = 0
    graph = dict()
    count = 0
    for i in range(n):
        _min = MAX
        for j in range(n):
            count+=1
            if i != j:
                cost = calculate_cost(arr[i], arr[j])
                if cost <= _min:
                    graph[i] = j
                    _min = cost                
                if cost == 0:
                    break
        print(_min, graph)
        answer += _min
    print(answer, count)
main()
'''