def solution(phone_number):

    return '*'*(len(phone_number)-4) + phone_number[-4:]

# 정규식 사용
import re

def solution(phone_number):
    return re.sub(r'\d(?=\d{4})','*',phone_number)