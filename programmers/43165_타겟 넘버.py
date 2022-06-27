def operator(idx, numbers, target, answer):
        if idx < len(numbers):
            numbers[idx] *= 1
            operator(idx+1, numbers, target, answer)            
            numbers[idx] *= -1
            operator(idx+1, numbers, target, answer)  
        elif sum(numbers) == target:            
            answer.append(1)
            
def solution(numbers, target):
    answer = list()
    operator(0, numbers, target, answer)
    return len(answer)