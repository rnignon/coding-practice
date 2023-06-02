def solution() :
    n = int(input())
    nums = [input().split() for i in range(n)]
    nums = sorted(nums, key=lambda x: (int(x[1]), int(x[0])))
    for num in nums : print(num[0], num[1])
    
solution()
