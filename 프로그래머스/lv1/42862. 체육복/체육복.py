def solution(n, lost, reserve):
    stu = [0 for _ in range(n)]
    for i in lost :
        stu[i-1] -= 1
    for i in reserve :
        stu[i-1] += 1
        
    for i in range(len(stu)) :
        if stu[i] >= 1 :
            if i > 0 and stu[i-1] == -1 :
                stu[i] -= 1
                stu[i-1] += 1
            elif i < n - 1 and stu[i+1] == -1 :
                print(i, stu)
                stu[i] -= 1 
                stu[i+1] += 1
    return sum([1 for s in stu if s >= 0])