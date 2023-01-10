n = int(input())
for _ in range(n):
    t = int(input())
    test = list(map(int, input().split()))
    count = 0
    for i in range(t):
        if test[i] % 2 != 0:
            count += 1
    print(count)