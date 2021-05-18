import itertools


def solution(numbers):
    answer = []

    numbers = list(itertools.permutations(numbers, 2))
    for i, j in numbers:
        answer.append(i + j)

    answer = sorted(set(answer))

    return answer