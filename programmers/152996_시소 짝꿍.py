from collections import Counter

def solution(weights):
    answer = 0
    
    duplicate_w = Counter()
    for i, v in Counter(weights).items():
        if v > 1:
            duplicate_w[i] = v
        
    multiple_w = Counter()
    for i, v in Counter(weights).items():
        multiple_w[i*2] += v
        multiple_w[i*3] += v
        multiple_w[i*4] += v
    
    for v in multiple_w.values():
        if v > 1:
            answer += (v*(v-1))//2
    for v in duplicate_w.values():
        answer -= v*(v-1)

    return answer
  
  
'''
# 첫 번째 
from itertools import combinations
from collections import Counter

def solution(weights):
    cnt = 0
    weights = Counter(weights)
    for a, b in combinations(weights.keys(), 2): # 서로 다른 무게
        if a*2 == b*3 or a*2 == b*4 or a*3 == b*4 or b*2 == a*3 or b*2 == a*4 or b*3 == a*4:
            cnt += weights[a] * weights[b]
    for v in weights.values(): # 같은 무게
        if v > 1:
            cnt += sum([i for i in range(1, v)])
    return cnt
  
  '''
