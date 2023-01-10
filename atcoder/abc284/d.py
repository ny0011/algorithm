from math import sqrt, pow

T = int(input())
answer = list()

for _ in range(T):
    n = int(input())
    m = int(pow(n, 1/3))
    for i in range(2, m+1):
        if (n % i == 0): 
            if (n % (i*i) == 0) :
                answer.append([i, n//(i*i)])
            else:
                answer.append([int(sqrt(n/i)),i])
            break
    
for i in range(T):
    print(answer[i][0], answer[i][1])