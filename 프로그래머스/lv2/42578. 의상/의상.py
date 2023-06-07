import itertools as it
def solution(clothes):
    clothes_dict = {}
    for i in clothes :
        if i[1] in clothes_dict :
            clothes_dict[i[1]].append(i[0])
        else :
            clothes_dict[i[1]] = [0, i[0]]
    answer = 1
    for i in clothes_dict :
        answer *= len(clothes_dict[i])
    return answer - 1