from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        count = Counter()
        for order in orders:
            count.update(combinations(sorted(list(order)),i))
        if not count:
            break
        count = count.most_common()
        frequent = count[0][1]
        if frequent < 2:
            continue
        for order in count:
            if order[1] == frequent:
                answer.append(''.join(order[0]))
                continue
            else:
                break
    return sorted(answer)
