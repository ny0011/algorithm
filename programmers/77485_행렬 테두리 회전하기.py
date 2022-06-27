def find_min_for_border_line(board, query):
    index_set = [-1]*4
    x1, y1, x2, y2 = [i+j for i,j in zip(index_set, query)]
    _min = board[x1][y1]

    # todo : 지정 위치로 이동 + 이동한 것 중 최소값 구하기
    # 1. 왼 -> 오
    dumped_1 = board[x1][y2]
    for y in range(y2,y1,-1):
        board[x1][y] = board[x1][y-1]
        _min = min(_min, board[x1][y])
    
    # 2. 오위 -> 오아래
    dumped_2 = board[x2][y2]
    for x in range(x2, x1+1, -1):
        board[x][y2] = board[x-1][y2]
        _min = min(_min, board[x][y2])
    board[x1+1][y2] = dumped_1
    
    # 3. 오아래 -> 왼아래
    dumped_3 = board[x2][y1]
    for y in range(y1, y2-1):
        board[x2][y] = board[x2][y+1]
        _min = min(_min, board[x2][y])
    board[x2][y2-1] = dumped_2
    
    # 4. 왼아래 -> 왼위
    for x in range(x1, x2-1):
        board[x][y1] = board[x+1][y1]
        _min = min(_min, board[x][y1])
    board[x2-1][y1] = dumped_3
    
    return min(_min, dumped_1, dumped_2, dumped_3)

def solution(rows, columns, queries):
    answer = []
    board = [[i*columns+j for j in range(1,columns+1)] for i in range(rows)]
    for i in range(len(queries)):
        _min = find_min_for_border_line(board, queries[i])
        answer.append(_min)
    
    return answer