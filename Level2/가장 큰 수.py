def solution(numbers):

    if sum(numbers) == 0:
        return 0

    numbers = list(map(str, numbers))
    tmp = []

    for i in range(len(numbers)):
        num = numbers[i]
        tmp.append((num * 4, num))

    numbers = sorted(tmp, reverse=True)
    answer = ''.join(numbers[i][1] for i in range(len(numbers)))

    return answer