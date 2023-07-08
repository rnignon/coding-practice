def solution():
    n = int(input())
    count = 1
    i = 1
    while count < n :
        count += i * 6
        i += 1
    print(i)
solution()
