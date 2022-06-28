MAX = 2000000001
def calculate_cost(p1, p2):
    return min(abs(p1[0]-p2[0]),abs(p1[1]-p2[1]),abs(p1[2]-p2[2]))

def main():
    n = int(input())
    arr = list()
    for _ in range(n):
        arr.append(list(map(int, input().split(" "))))

    answer = 0
    connected = [0] * (n)
    for i in range(n):
        _min = MAX
        for j in range(n):
            if i != j:
                cost = calculate_cost(arr[i], arr[j])
                if cost < _min:
                    connected[i] = j
                    _min = cost
        print(_min, connected)
        answer += _min
    print(answer)
main()