from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = list()
    maxOrderLength = len(max(orders, key= lambda order: len(order)))
    real_course = list(filter(lambda c: c <= maxOrderLength, course))

    for c in real_course:
        comb = list()
        for order in orders:
            comb += combinations(sorted(order), c)
        new_courses = Counter(comb)
        
        _max = max(new_courses.values())
        if _max >= 2:
            answer+=["".join(menu)  for menu in new_courses if new_courses[menu] == _max]                    
            
    return sorted(answer)