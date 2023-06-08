from math import ceil
def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)) :
        days.append(ceil((100 - progresses[i]) / speeds[i]))
    answer = []
    pre = 0
    for i in days :
        if pre >= i :
            answer[-1] += 1
        else :
            answer.append(1)
            pre = i
    return answer