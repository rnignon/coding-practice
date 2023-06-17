from collections import deque
from sys import stdin
def solution() :
    n = int(stdin.readline())
    queue = deque([])
    for i in range(n) :
        command = stdin.readline()
        if 'push' in command :
            queue.append(command.split()[-1])
        elif 'pop' in command :
            if len(queue) == 0 :
                print(-1)
            else :
                print(queue.popleft())
        elif 'size' in command :
            print(len(queue))
        elif 'empty' in command :
            if len(queue) == 0 :
                print(1)
            else :
                print(0)
        elif 'front' in command :
            if len(queue) == 0 :
                print(-1)
            else :
                print(queue[0])
        elif 'back' in command :
            if len(queue) == 0 :
                print(-1)
            else :
                print(queue[-1])
            
solution()
