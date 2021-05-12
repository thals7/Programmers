# # # 2019 카카오 개발자 겨울 인턴십

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


# 정규 표현식 이용한 풀이

from collections import Counter
import re

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, sorted(s, key = lambda x:s[x], reverse = True)))

# most_common() 함수 이용하여 가장 흔한 요소부터 적은 것 순으로 나열하는 리스트 반환
def solution(s):

    s = Counter(re.findall('\d+', s)).most_common()
    return list(map(int, list(i[0] for i in s)))