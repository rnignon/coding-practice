def solution(citations):
    citations = sorted(citations)
    answer = []
    length = max(citations)
    for i in range(length + 1) :
        count = 0
        for j in citations :
            if i <= j :
                count += 1
        if count >= i :
            answer.append(i)
    return max(answer)