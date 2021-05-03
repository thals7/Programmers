def solution(a, b):
    answer = ''
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = b
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]

    for i in range(a - 1):
        day += month[i]
    answer = week[day % 7]

    return answer