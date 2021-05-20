from collections import deque

def solution(bridge_length, weight, truck_weights):

    answer = 0
    w = 0
    q = deque([])

    while truck_weights:
        if len(q) == bridge_length:
            pop = q.popleft()
            w -= pop
        if w + truck_weights[-1] <= weight:
            truck = truck_weights.pop()
            q.append(truck)
            w += truck
        else:
            q.append(0)
        answer += 1

    return answer + bridge_length