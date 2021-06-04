from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while people:
        boat = limit - people.pop()
        if people and boat - people[0] >= 0:
            people.popleft()
        answer += 1

    return answer