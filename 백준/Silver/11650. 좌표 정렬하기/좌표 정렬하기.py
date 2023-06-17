from sys import stdin
def solution() :
    n = int(stdin.readline())
    coor = []
    for i in range(n) :
        x, y = map(int, stdin.readline().split())
        coor.append([x, y])
    sorted_coor = sorted(coor, key=lambda x:(x[0], x[-1]))
    for i in sorted_coor :
        print(i[0], i[1])
solution()
