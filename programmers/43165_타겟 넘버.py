def create_list(numbers):
    new = list()
    idx = 0
    while idx < len(numbers):
        if len(new) == 0:
            number = numbers[idx]
            new.append(number)
            new.append(-number)
            idx += 1
            continue
        length = len(new)
        tmp = list()
        number = numbers[idx]
        for i in range(length):
            tmp.append(new[i]+number)
        for i in range(length):
            tmp.append(new[i]-number)
        new = tmp
        idx += 1 
    return new
    
def solution(numbers, target):
    sum_list = create_list(numbers)
    return sum_list.count(target)