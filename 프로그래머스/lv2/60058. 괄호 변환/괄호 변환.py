def solution(p):
    answer = ''
    if p == '' : answer = ''
    else : answer = balance(p)
    return answer

def balance (p) :
    if p == '' : return ''
    u = ''
    v = p
    for i in range(1, len(v) + 1) :
        if v[:i].count('(') == v[:i].count(')') :
            u = v[:i]
            v = v[i:]
            break
    return correct(u, v)

def correct (u, v) :
    stack = []
    cor = True
    for i in u :        
        if i == ')' :
            if len(stack) == 0 : cor = False
            else : stack.pop()
        else : stack.append('(')
    if cor :
        s = u + balance(v)
    else :        
        s = '(' + balance(v) + ')'
        s += ''.join('(' if i == ')' else ')' for i in u[1:-1])
    return s