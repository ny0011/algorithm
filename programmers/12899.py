'''
0, 1, 2 대신
1, 2, 4 로 수를 표현

원래 수는 0이 제일 첫번째 자리수가 될 수 없음 
하지만 0을 첫번째 자리수로 생각한다면 아래처럼 구성할 수 있음

1 ~ 3   
0 ~ 2
 
 4 ~ 12  
00 ~ 22

 13 ~  39 
000 ~ 222

1 = (1-1)x3^0
2 = (2-1)x3^0
3 = (3-1)x3^0
4 = (4-1)x3^0 = (3 + 1-1)x3^0 = 3^1x3^0 + (1-1)x3^0  = (1-1)x3^1 + (1-1)x3^0
5 = (5-1)x3^0 = (3 + 2-1)x3^0  = (1-1)x3^2 + (2-1)x3^0

.. 
이렇게 몫에 계속 1을 빼주면 됨
'''


def solution(n):
    answer = ''
    while n != 0:
        n -= 1
        r = n % 3
        n = n // 3 
        answer = '124'[r] + answer            
        
    return answer