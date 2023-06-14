from itertools import permutations
def solution(k, dungeons):
    max_v = 0
    for i in permutations(dungeons, len(dungeons)) :
        cnt = 0
        l = k
        for j in i :
            if l >= j[0] :
                cnt += 1
                l -= j[1]
        if cnt > max_v :
            max_v = cnt
    return max_v