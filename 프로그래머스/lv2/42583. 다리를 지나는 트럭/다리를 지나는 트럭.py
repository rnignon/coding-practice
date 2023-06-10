from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    sum_w = 0
    while bridge :
        time += 1
        sum_w -= bridge.popleft()
        if trucks :
            if sum_w + trucks[0] > weight :
                bridge.append(0)
            else :
                sum_w += trucks[0]
                bridge.append(trucks.popleft())
    return time