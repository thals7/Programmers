def solution(number, k):
    answer = []
    for i in number:
        while answer and i > answer[-1] and k > 0:
            answer.pop()
            k -= 1
        answer.append(i)
    if k > 0:
        answer = answer[:len(answer)-k]
    return ''.join(answer)