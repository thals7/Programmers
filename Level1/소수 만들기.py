from itertools import combinations
import math


def solution(nums):
    answer = 0
    combi = list(map(sum, combinations(nums, 3)))

    for num in combi:
        prime = True
        if num % 2 == 1 and num > 2:
            for i in range(3, math.ceil(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                answer += 1
        elif num == 2:
            answer += 1

    return answer