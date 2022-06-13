# 굿 테스트케이스 : solution("aaaaaaaaaaaabcd");  // 6

def CompressNumCharacter(s, n):
    c = s[:n]
    new_s = [[c,1]]
    new_s_index = 0
    new_s_count = 1
    s_length = len(s)
    for i in range(n,s_length,n):
        value = s[i:i+n]
        if i+n > s_length:
            value = s[i:s_length]
            
        if c == value:
            new_s[new_s_index][new_s_count] += 1              
        else:
            c = value
            new_s_index += 1 
            new_s.append([c,1])
    
    check_str = str()
    for arr in new_s:
        for v in arr:
            if v != 1:
                check_str += str(v)
    return len(check_str)

def solution(s):
    return min(CompressNumCharacter(s,i) for i in range(1, len(s)//2 + 2 ))