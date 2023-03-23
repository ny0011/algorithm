h, w = map(int, input().split())
a = list()
for _ in range(h):
    a.append(list(map(int, input().split())))
    
    
for i in range(h):
    for j in range(w):
        if a[i][j] != 0:
            print(chr(ord('A')+a[i][j]-1), end="")
        else:
            print(".", end="")
    print("")
    
