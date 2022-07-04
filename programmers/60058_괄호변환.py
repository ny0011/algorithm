def is_right_string(p):
    stack = []
    for s in p:
        if s == "(":
            stack.append(s)
        else:
            if len(stack) == 0: return False
            stack.pop()
    if len(stack) == 0: return True
    return False


def divide_string(p):
    u = ""
    v = ""
    count = 0
    for s in p:
        u += s
        if s == "("   : count+=1
        else      : count-=1       
        if count == 0 : break
    v = p[len(u):]
    return u, v

def convert_right_string(p): 
    if len(p) == 0:
        return p
    
    u, v = divide_string(p)
    
    if is_right_string(u):
        substring = convert_right_string(v)
        return u+substring 
    else:
        substring = convert_right_string(v)
        u_delete = u[1:len(u)-1]
        u_inverse = "".join([ ")" if s == "("  else "(" for s in u_delete ])
        return "("+substring+")"+u_inverse

def solution(p):
    return convert_right_string(p)