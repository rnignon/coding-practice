import heapq
def solution(n, works):
    heap = []
    for i in works :
        heapq.heappush(heap, -i)
    print(heap)
    for i in range (n) :
        max_v = -heapq.heappop(heap)
        if max_v > 0 :
            heapq.heappush(heap, -(max_v-1))
        else :
            heapq.heappush(heap, -max_v)
    return sum(i ** 2 for i in heap)