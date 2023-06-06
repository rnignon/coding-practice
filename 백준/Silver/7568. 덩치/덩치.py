from sys import stdin
def solution () :
    n = int(input())
    builds = []
    answer = []
    for i in range(n) :
        w, h = map(int, stdin.readline().split())
        builds.append([w, h])
    for i in range(n) :
        count = 1
        for j in range(n) :
            if builds[i][0] < builds[j][0] and builds[i][1] < builds[j][1] :
                count += 1
        answer.append(str(count))
    print(' '.join(answer))
solution()