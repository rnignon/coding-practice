from collections import deque
def solution(stones, k):
    q = deque()
    stones_max = []
    stones_len = len(stones)
    # O(n)
    for i in range (stones_len) :
        if q and i >= (k + q[0]) :
            q.popleft()
        while q :
            if (stones[i] > stones[q[-1]]) :
                q.pop()
            else : break
        q.append(i)
        if i >= (k - 1) :
            stones_max.append(stones[q[0]])
    return min(stones_max)