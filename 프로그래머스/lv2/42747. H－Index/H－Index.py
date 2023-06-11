def solution(citations):
    citations = sorted(citations)
    answer = [0]
    length = len(citations)
    for i in range(length) :
        if citations[i] >= length - i :
            answer.append(length - i)
            print(length - i)
    return max(answer)