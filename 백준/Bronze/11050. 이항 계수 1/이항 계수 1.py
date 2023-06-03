import math

def solution() :
    n, k = map(int, input().split())
    print(math.comb(n, k))

solution()
