def find_gcd(a,b):
    while b:
        a, b = b, a%b
    return a

def solution(w,h):
    _min = min(w,h)
    _max = max(w,h)
    if _min == 1 :
        return 0
    
    value = find_gcd(_max, _min)
    if value != 1:
        return _max * _min - (_max + _min - value) 
    return _max * _min - (_max+_min-1)
    
