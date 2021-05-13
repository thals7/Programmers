import re

# 1. 정규식 사용
def solution(phone_book):
    answer = True
    # 짧은 숫자부터 앞에 나올 수 있게 정렬
    # 이 때 phone_book 에 들어있는 번호가 숫자가 아닌 문자열이므로 sort를 할 경우 문자로 취급되어 맨 앞자리부터 숫자의 크기 기준으로 정렬됨
    # ex) ["12","123","1235","567","88"] -> ['12', '123', '1235', '567', '88']
    phone_book.sort()

    for i in range(len(phone_book)-1):
            # 정렬된 상태이므로 바로 뒤에 있는 숫자 하나만 비교해도 됨
            if re.match(phone_book[i], phone_book[i+1]) is not None:
                answer = False
                return answer

    return answer

# 2. 문자열 끊어서
def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
            if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
                answer = False
                return answer

    return answer