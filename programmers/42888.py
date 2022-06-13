ENTER = "Enter"
LEAVE = "Leave"
CHANGE = "Change"


def set_db(text, nameDB):
    words = text.split(' ')
    if words[0] == LEAVE:
        return
    cmd, uid, name = words
    nameDB[uid] = name  

def print_msg(text, nameDB):
    words = text.split(' ')
    if words[0] == CHANGE:
        return None
    uid = words[1]
    if words[0] == ENTER:
        return f"{nameDB[uid]}님이 들어왔습니다."
    if words[0] == LEAVE:
        return f"{nameDB[uid]}님이 나갔습니다."

def solution(record):
    nameDB = dict()
    answer = list()
    for text in record:
        set_db(text, nameDB)
    
    for text in record:
        msg = print_msg(text, nameDB)
        if msg != None:
            answer.append(msg)
    
    return answer