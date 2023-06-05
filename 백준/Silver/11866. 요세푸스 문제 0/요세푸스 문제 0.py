def solution () :
    n, k = map(int, input().split())
    queue = [i for i in range(1, n + 1)]
    answer = "<"
    while queue :
        for i in range (k - 1) :
            queue.append(queue.pop(0))
        answer += str(queue.pop(0)) + ", "
    answer = answer[:-2] + ">"
    print(answer)
solution()
