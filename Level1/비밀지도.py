# 2018 KAKAO BLIND RECRUITMENT

# 처음 풀이
def binary(n, fixedLen):
    if n == 0:
        return '0'*fixedLen
    result = ''

    while n > 1:
        result = str(n % 2) + result
        n = n // 2

    result = '1' + result

    if len(result) < fixedLen:
        result = '0' * (fixedLen - len(result)) + result

    return result


def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        result = ''
        b1 = binary(arr1[i], n)
        b2 = binary(arr2[i], n)
        print(b1, b2)
        for j in range(n):
            if b1[j] + b2[j] == "00":
                result += ' '
            else:
                result += '#'
        answer.append(result)

    return answer


# 함수 이용
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        b = str(bin(i|j)[2:]) # i|j = i 또는 j 가 1이면 1

        b = b.rjust(n,'0') # 오른쪽으로 정렬 후 n에서 남은 공백만큼 입력한 문자로 채움
        # 또는 b.zfill(n) (n에서 남은 공백만큼 0을 왼쪽에 채워줌)

        b = b.replace('1', '#')
        b = b.replace('0', ' ')

        answer.append(b)

    return answer
