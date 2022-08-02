from copy import deepcopy

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def move(checked, axis, answer):
    x, y = axis
    stack = []
    n = len(checked[0])-1
    m = len(checked)-1
    for i in range(len(dx)):
        ix = x+dx[i]
        iy = y+dy[i]
        if ix > n or ix < 0 or iy > m or iy < 0:
            continue
        if checked[ix][iy]==0:
            continue
        
        checked[ix][iy] = 0
        answer += 1
        move( checked, (ix, iy), answer)
    



def solution(maps):
    answer = 0
    n = len(maps[0])-1
    m = len(maps)-1
    checked = deepcopy(maps)
    stack = [(0, 0)]
    
    while stack:
        x, y = stack.pop()
        if checked[x][y] == 1:
            checked[x][y] = 0
            for i in range(len(dx)):
                ix = x+dx[i]
                iy = y+dy[i]
                if ix > n or ix < 0 or iy > m or iy < 0:
                    continue
                if checked[ix][iy]==0:
                    continue
                stack.append((ix, iy))
                answer += 1            
            
    
    if checked[n][m] == 0:
        return answer
    else:
        return -1

a=solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
print(a)