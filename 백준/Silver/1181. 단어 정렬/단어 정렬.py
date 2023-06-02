def solution() :
    n = int(input())
    dic = set([input() for i in range(n)])
    dic = sorted(dic, key=lambda x: (len(x), x))
    for i in dic : print(i)
    
solution()
