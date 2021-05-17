import math, itertools


def solution(numbers):
    answer = 0
    nums = []

    # 순열
    for i in range(1, len(numbers) + 1):
        nums = nums + list(map(''.join,itertools.permutations(list(numbers), i)))
    # 0으로 시작하는 숫자 제거한 뒤 중복 제거
    nums = set(map(int,nums))

    # 소수 찾기
    for i in nums:
        if i == 2:
            answer += 1
            continue
        if i < 2 or i%2 == 0:
            continue
        prime = True
        for j in range(3,int(math.sqrt(i))+1,2):
            if i%j == 0:
                prime = False
                break
        if prime:
            answer += 1

    return answer


print(solution("011"))