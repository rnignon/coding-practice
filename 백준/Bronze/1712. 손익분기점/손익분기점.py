def solution():
    a, b, c = map(int, input().split())
    answer = a // (c - b) + 1 if (c - b) > 0 else -1
    print(answer)
solution()
