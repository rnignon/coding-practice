from collections import deque
def solution(n, m, section):
    section = deque(section)
    answer = 0
    while section :
        index = section.popleft()
        while section :
            s = section.popleft()
            if s >= index + m :
                section.appendleft(s)
                break
        answer += 1
    return answer