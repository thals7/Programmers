def solution(brown, yellow):
    answer = []

    for w in range(5000):
        for h in range(w + 1):
            if brown == (2 * w) + (2 * (h - 2)) and yellow == (w - 2) * (h - 2):
                answer.append(w)
                answer.append(h)
                return answer