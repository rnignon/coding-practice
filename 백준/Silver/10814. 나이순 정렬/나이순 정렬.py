def solution() :
    user = {}
    case = int(input())
    for i in range(case) :
        user[i] = input().split()
    user = sorted(user.items(), key=lambda x : (int(x[1][0]), x[0]))
    for i in user : print(i[1][0], i[1][1])
solution()
