def solution(s) :
    stack = []
    for j in s :
        if j == '(' :
            stack.append('(')
        elif j == ')' :
            if len(stack) == 0 :
                return False
            else :
                stack.pop()
    answer = False
    if len(stack) == 0 : answer = True
    return answer