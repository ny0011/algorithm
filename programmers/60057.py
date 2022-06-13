# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057
# 굿 테스트케이스 : solution("aaaaaaaaaaaabcd");  // 6

def CompressNumCharacter(s, n):
    c = s[:n]
    check = [c]
    count = 1
    s_length = len(s)
    for i in range(n,s_length,n):
        value = s[i:i+n]
        if i+n > s_length:
            value = s[i:s_length]
        if c == value:
            count += 1              
        else:            
            if count != 1:
                check.append(str(count))
            c = value
            count = 1
            check.append(value)
    if count != 1:
        check.append(str(count))
    check_str = ''.join(check)
    if len(check_str) != len(s):
        return len(check_str)
    return len(s)

def solution(s):
    answer = len(s)
    mid = len(s)//2 + 1
    for i in range(1, mid):
        ret = CompressNumCharacter(s,i)
        if answer > ret:
            answer = ret
    
    return answer
