# 2019 카카오 개발자 겨울 인턴십

def solution(s):
    num = ""
    dic = {}

    for char in s:
        if char == "{" or char == "}":
            continue
        if char == ",":
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
            num = ""
            continue
        num = num + char

    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

    dic = sorted(dic, key=lambda x:dic[x], reverse = True)
    answer = list(map(int,dic))

    return answer