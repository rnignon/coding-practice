def solution () :
    stack = []
    answer = []
    index = 0
    
    for i in range (int(input())) :
        n = int(input())
        if n > index :
            for j in range (n - index) :
                stack.append(index + j + 1)
                answer.append('+')
            index = stack[-1]

        if n == stack[-1] :
            stack.pop()
            answer.append('-')
        else :
            print("NO")
            return
    for i in answer : print(i)

solution()