# 처음 풀이
def solution(n):
    if n == 0: return 0
    answer = n+1
    sqrt = int(n**0.5)
    for i in range(2,sqrt+1):
        if n%i == 0:
            answer += (i+n//i)
    if sqrt**2 == n:
        answer -= sqrt
    return answer


# 추가 풀이
def solution2(n):
    if n == 0: return 0
    sqrt = int(n**0.5)
    answer = sum([i+n//i for i in range(1,sqrt+1) if n%i == 0])
    return answer-sqrt if sqrt**2 == n else answer