import re

def solution(record):
    answer = []
    dic = {}
    id_record = []

    for data in record:
        rec = data.split()
        if rec[0] == 'Enter':
            if rec[0] not in dic:
                dic[rec[1]] = rec[2]
            id_record.append(rec[1]+"님이 들어왔습니다.")
        elif rec[0] == 'Leave':
            id_record.append(rec[1]+"님이 나갔습니다.")
        elif rec[0] == 'Change':
            dic[rec[1]] = rec[2]

    for data in id_record:
        id = re.match('[a-zA-Z0-9]+',data).group()
        answer.append(data.replace(id,dic[id]))

    return answer


# 정규표현식 빼고 효율성 개선
def solution(record):
    answer = []
    dic = {}

    for data in record:
        rec = data.split()
        if rec[0] != 'Leave':
            dic[rec[1]] = rec[2]

    for data in record:
        rec = data.split()
        if rec[0] == 'Enter':
            answer.append(dic[rec[1]] + '님이 들어왔습니다.')
        elif rec[0] == 'Leave':
            answer.append(dic[rec[1]] + '님이 나갔습니다.')

    return answer