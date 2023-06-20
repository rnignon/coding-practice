def solution(a, b):
    if b < a :
        tmp = b
        b = a
        a = tmp
    answer = [i for i in range(a, b+1)]
    return sum(answer)