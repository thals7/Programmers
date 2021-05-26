# 1
def solution(d, budget):
    answer = 0
    d.sort(reverse=True)
    length = len(d)

    while length > 0 and d[-1] <= budget:
        price = d.pop()
        answer += 1
        budget -= price
        length -= 1

    return answer

# 2
def solution(d,budget):
    answer = 0
    d.sort()

    for i in d:
        if budget >= i:
            budget -= i
            answer += 1
        else: break

    return answer