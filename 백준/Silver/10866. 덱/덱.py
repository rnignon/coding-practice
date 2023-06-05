import sys
def solution () :
    n = int(input())
    deque = []
    for i in range (n) :
        command = sys.stdin.readline().split()
        if 'push_front' == command[0] :
            deque.insert(0, int(command[1]))
        elif 'push_back' == command[0] :
            deque.append(int(command[1]))
        elif 'pop_front' == command[0] :
            print(-1 if len(deque) == 0 else deque.pop(0))
        elif 'pop_back' == command[0] :
            print(-1 if len(deque) == 0 else deque.pop())
        elif 'size' == command[0] :
            print(len(deque))
        elif 'empty' == command[0] :
            print(1 if len(deque) == 0 else 0)
        elif 'front' == command[0] :
            print(-1 if len(deque) == 0 else deque[0])
        elif 'back' == command[0] :
            print(-1 if len(deque) == 0 else deque[-1])
solution()
