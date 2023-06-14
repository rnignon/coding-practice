from collections import deque
def solution(n, wires):
    answer = n
    line = {}
    for i in range(n+1) :
        line[i+1] = []
    for wire in wires :
        line[wire[0]].append(wire[1])
        line[wire[1]].append(wire[0])
    
    for line1, line2 in wires :
        visit = [False for i in range(n+1)]
        queue = deque()
        queue.append(line1)
        connect = 1
        visit[line1] = True
        visit[line2] = True
        
        while queue :
            i = queue.popleft()
            for j in line[i] :
                if not visit[j] :
                    connect += 1
                    visit[j] = True
                    queue.append(j)
        diff = [connect, n-connect]
        diff = sorted(diff)
        if answer > diff[1] - diff[0] :
            answer = diff[1] - diff[0]
        
    return answer