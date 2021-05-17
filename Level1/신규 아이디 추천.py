import re

def solution(new_id):

    answer = new_id.lower()  # 1단계
    answer = re.sub('[^a-z0-9-_.]', '', answer) # 2단계
    answer = re.sub('[..]+','.', answer) # 3단계
    # answer = re.sub('\.+','.', answer)
    answer = answer.strip(".") # 4단계
    # answer = re.sub('^[.][.]$','.', answer)

    if not answer: # 5단계
        answer = "a"

    if len(answer) >= 16: # 6단계
        answer = answer[:15]
        answer = answer.rstrip(".")

    while len(answer) < 3: # 7단계
        answer = answer + answer[-1]

    return answer