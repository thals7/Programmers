def solution(n):
    tmp = ''
    answer = 0

    while n > 2:
        tmp = str(n%3) + tmp
        n //= 3
    tmp = str(n) + tmp

    t = 1
    for i in tmp:
        answer += int(i) * t
        t *= 3
    # int(num,base) -> 진법 변환 가능
    # answer = int(tmp,3)

    return answer