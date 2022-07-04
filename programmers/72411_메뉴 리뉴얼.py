    # course 최대 수가 order 최대 길이보다 작은 것만 course 돌리기
    # order의 course 수 만큼 조합 구하기
    # 조합 하나가 order에 2개 이상? ok > answer에 추가, ng > 다음
    # course 수보다 order 
from itertools import combinations

def solution(orders, course):
    answer = list()
    maxOrderLength = len(max(orders, key= lambda order: len(order)))
    real_course = list(filter(lambda c: c <= maxOrderLength, course))
    order_set = sorted(list(set("".join(orders))))

    for c in real_course:
        _max_list = list()
        _max_count = 0
        _test = list(combinations(order_set, c))
        for t in _test:
            new_course = ''.join(t)  
            count = 0
            for check in orders:
                isOrdered = False
                for n in new_course:
                    if n not in check:
                        isOrdered = False
                        break
                    else:
                        isOrdered = True
                if isOrdered:
                    count += 1
            if count < 2:
                continue   
            if _max_count < count:
                _max_count = count
                _max_list = [new_course]
            elif _max_count == count:
                _max_list.append(new_course)
        if _max_count >= 2:
            for item in _max_list:
                answer.append(item)
    answer.sort()
    return answer