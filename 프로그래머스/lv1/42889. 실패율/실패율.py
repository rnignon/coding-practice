def solution(N, stages):
    p_count = len(stages)
    fail = [0 for i in range(N)]
    for i in range(N) :
        count = stages.count(i+1)
        fail[i] = count / p_count if p_count != 0 else 0
        p_count -= count
    answer = [0 for i in range(N)]
    for i in range(N) :
        max_index = fail.index(max(fail))
        answer[i] = max_index + 1
        fail[max_index] = -1
    return answer