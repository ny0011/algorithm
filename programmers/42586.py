def populate_date(progress, speed):
    q, r = divmod(100 - progress, speed) 
    return q + bool(r)

def solution(progresses, speeds):
    dates = []
    for i in range(len(speeds)):
        dates.append(populate_date(progresses[i], speeds[i]))
    top = dates.pop(0)
    answer = [1]
    i_answer = 0
    while len(dates) > 0:
        if top < dates[0]:            
            top = dates.pop(0)
            answer.append(1)
            i_answer +=1
        else:
            answer[i_answer] +=1
            dates.pop(0)
    return answer
