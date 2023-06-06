from sys import stdin
def solution () :
    n = int(input())
    nums = [0] * 100001
    for i in range(n) :
        nums[int(stdin.readline())] += 1
    for i in range(10001) :
        if nums[i] != 0 :
            for j in range(nums[i]) :
                print(i)
solution()
