def solution(s):
    s = s.lower()
    answer = s[0].upper()
    for c in s[1:]:
        if answer[-1] == ' ':
            answer += c.upper()
        else:
            answer += c
    return answer

def solution2(s):
    return ' '.join([w.capitalize() for w in s.split(' ')])