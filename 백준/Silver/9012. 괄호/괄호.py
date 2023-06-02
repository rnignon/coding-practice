def solution () :
    for i in range (int(input())) :
        stack = []
        corr = True
        p = input()
        for j in p :
            if j == '(' :
                stack.append('(')
            elif j == ')' :
                if len(stack) == 0 :
                    corr = False
                else :
                    stack.pop()
        if len(stack) != 0 or not corr : print("NO")
        else : print("YES")
        
solution()
