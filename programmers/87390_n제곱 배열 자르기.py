# 4 5 6 [2,3]
def n_square_to_n(answer, start, end, row):
    for k in range(start, end):
        if row < k:
            answer.append(k+1)
        else:
            answer.append(row+1)

def solution(n, left, right):
    answer = []
    left_r, left_q = divmod(left, n)    
    right_r, right_q = divmod(right, n)
    if left_r == right_r:
        n_square_to_n(answer, left_q, right_q+1, left_r)
        return answer
    
    n_square_to_n(answer, left_q, n, left_r)
    for next_n in range(left_r+1, right_r):
        n_square_to_n(answer, 0, n, next_n)
    
    right_start = right_r * n
    n_square_to_n(answer, 0, right-right_start+1, right_r)

    
    return answer
  
  
  # refactor
  
  def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        r, q = divmod(i, n)
        answer.append(max(r, q)+1)

    
    return answer
