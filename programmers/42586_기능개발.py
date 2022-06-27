def populate_date(progress, speed):
    q, r = divmod(100 - progress, speed) 
    return q + int(bool(r))

def solution(progresses, speeds):
    answer = []
    max = 0
    for i in range(len(speeds)):
        top = populate_date(progresses[i], speeds[i])
        if len(answer) == 0 or max < top:
            max = populate_date(progresses[i], speeds[i])
            answer.append(1)
        else:
            answer[-1]+=1
    return answer