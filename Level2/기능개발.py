import math

def solution(progresses, speeds):
    answer = [0] * 99
    days = math.ceil((100 - progresses[0])/speeds[0])

    for i in range(len(progresses)):
        tmp = math.ceil((100 - progresses[i])/speeds[i])
        if days < tmp:
            days = tmp
        answer[days] += 1

    while 0 in answer:
        answer.remove(0)

    return answer