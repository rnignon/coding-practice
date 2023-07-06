from itertools import combinations
def solution():
    n, m = map(int, input().split())
    nums = [int(i) for i in input().split()]
    max_v = 0
    
    for i in combinations(nums, 3) :
        sum_v = sum(i)
        if sum_v <= m and sum_v > max_v :
            max_v = sum_v
    print(max_v)

solution()
