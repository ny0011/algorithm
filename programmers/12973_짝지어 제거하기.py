def solution(s):
    stack = list()
    for v in s:
        if len(stack) == 0:
            stack.append(v)
        else:
            if stack[-1] == v:
                stack.pop()
            else:
                stack.append(v)
    if len(stack) == 0:
        return 1
    else:
        return 0