def solution(absolutes, signs):
    answer = 0
    for i, j in zip(absolutes, signs):
        answer = answer+i if j else answer-i

    return answer