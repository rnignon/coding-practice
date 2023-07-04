import heapq
def solution(operations):
    answer = []
    for operation in operations :
        if operation[0] == 'I' :
            heapq.heappush(answer, int(operation.split()[1]))
        elif operation == 'D 1' and answer :
            answer = sorted(answer)[:-1]
        elif operation == 'D -1' and answer:
            heapq.heappop(answer)
    return [max(answer), min(answer)] if answer else [0, 0]