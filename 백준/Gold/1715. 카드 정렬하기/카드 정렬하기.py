import heapq
def solution():
    n = int(input())
    nums = []
    for i in range(n) :
        heapq.heappush(nums, int(input()))
    count = 0
    while len(nums) > 1 :
        min_v = heapq.heappop(nums)
        min_v += heapq.heappop(nums)
        count += min_v
        heapq.heappush(nums, min_v)
    print(count)
solution()
