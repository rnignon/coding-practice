def solution(sizes):
    for i in range(len(sizes)) :
        if sizes[i][0] < sizes[i][1] :
            sizes[i] = [sizes[i][1], sizes[i][0]]
    a = 0
    b = 0
    for size in sizes :
        print(size)
        if size[0] > a :
            a = size[0]
        if size[1] > b :
            b = size[1]
    return a * b