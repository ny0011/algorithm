from functools import cmp_to_key

def sort_max_num(x, y):
    _x = x
    _y = y
    if _x[0] > _y[0]:
        return 1
    elif _x[0] < _y[0]:
        return -1
    else:
        if int(x+y) > int(y+x):
            return 1
        elif int(x+y) < int(y+x):
            return -1
        else: 
            return 0
        
def solution(numbers):
    answer = ''
    a = [str(n) for n in numbers]
    a.sort(reverse=True, key=cmp_to_key(sort_max_num))
    answer = ''.join(a)
    if answer.count('0') == len(answer):
        return '0'
    return answer
