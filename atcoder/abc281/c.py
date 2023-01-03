N, T = map(int, input().split())
a = list(map(int, input().split()))

i = 0
total = sum(a)
r, q = divmod (T, total)
count = r * N
T = q

if T == 0:
    print(1, 0)
    exit()

_min = 0
for j in range(N):
    _min = min(T, a[j])
    T -= _min
    count += 1
    if T == 0:
        i = j
        break
        
print(i+1, _min)