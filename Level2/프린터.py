from collections import deque

def solution(priorities, location):
    answer = 0
    index = -1
    p = deque(priorities)

    while p:
        index += 1
        cur_index = index % len(priorities)
        if priorities[cur_index] == 0:
            continue
        cur = p.popleft()
        printer = True
        for i in p:
            if i > cur:
                p.append(cur)
                printer = False
                break
        if not printer:
            continue
        answer += 1
        priorities[cur_index] = 0
        if cur_index == location:
            break

    return answer