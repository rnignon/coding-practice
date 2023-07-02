from itertools import product
def solution(numbers, target):
    nums = [[i, -i] for i in numbers]
    answer = 0
    for p in product(*nums) :
        if sum(p) == target :
            answer += 1
    return answer