from sys import stdin
def solution() :
    n = int(stdin.readline())
    stack = []
    for i in range(n) :
        command = stdin.readline()
        if 'push' in command :
            stack.append(command.split()[-1])
        elif 'pop' in command :
            if len(stack) == 0 :
                print(-1)
            else :
                print(stack.pop())
        elif 'size' in command :
            print(len(stack))
        elif 'empty' in command :
            if len(stack) == 0 :
                print(1)
            else :
                print(0)
        elif 'top' in command :
            if len(stack) == 0 :
                print(-1)
            else :
                print(stack[-1])
            
solution()
