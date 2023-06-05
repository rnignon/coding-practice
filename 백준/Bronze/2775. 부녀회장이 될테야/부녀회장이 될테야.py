def solution () :
    case = int(input())
    for c in range(case) :
        n = int(input())
        m = int(input())
        p = [i for i in range(1, m + 1)]
        for f in range(n) :
            for i in range(1, m) :
                p[i] += p[i-1]
        print(p[-1])
        
solution()