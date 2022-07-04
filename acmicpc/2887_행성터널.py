

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