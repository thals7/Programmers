import math

def solution(left, right):
    answer = 0

    for i in range(left,right+1):
        divisors = set()
        for j in range(1,math.ceil(math.sqrt(i)+1)):
            if i%j == 0:
                divisors.add(j)
                divisors.add(i//j)
        if len(divisors)%2 == 0:
            answer += i
        else:
            answer -= i

    return answer