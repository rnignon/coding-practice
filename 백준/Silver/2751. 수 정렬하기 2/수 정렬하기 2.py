from sys import stdin
def solution () :
    n = int(input())
    nums= []
    for i in range(n) :
        nums.append(int(stdin.readline()))
    nums.sort()
    for i in range(n) :
        print(nums[i])
solution()
