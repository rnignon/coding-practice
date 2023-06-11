import heapq
def solution(scoville, K):
    heap = []
    for i in scoville :
        heapq.heappush(heap, i)
    s_min = heap[0]
    count = 0
    while s_min < K :
        s_new = heapq.heappop(heap) + (heapq.heappop(heap) * 2)
        heapq.heappush(heap, s_new)
        s_min = heap[0]
        count += 1
        if len(heap) == 1 and heap[0] < K :
            return -1
    return count 