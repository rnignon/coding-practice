from sys import stdin
def solution():
    nums = [0] * 30
    for i in range (28) :
        nums[int(stdin.readline()) - 1] = 1
    for i in range (30) :
        if nums[i] == 0 :
            print(i + 1)
    
solution()
