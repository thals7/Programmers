# 효율성 실패

def solution(participant, completion):
    for name in completion:
        if name in participant:
            participant.remove(name)

    answer = participant[0]

    return answer

# 효율성 개선 (딕셔너리 이용)

def solution(participant, completion):

    answer = ''
    names = dict()

    for name in participant:
        if names.get(name,0) == 0:
            names[name] = 1
        else:
            names[name] += 1

    for name in completion:
        names[name] -= 1

    for name, cnt in names.items():
        if cnt == 1:
            answer = name

    return answer