def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    print(nums.count(target))
solution()
