def solution(arr):
    queue = []
    for i in arr :
        if i not in queue[-1:] :
            queue.append(i)
    return queue