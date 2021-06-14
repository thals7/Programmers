def isRight(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True

def solution(p):
    if not p:
        return ''
    cnt = 0
    u,v = '',''
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            u = p[0:i+1]
            v = p[i+1:]
            break
    if isRight(u):
        return u + solution(v)
    answer = '('+solution(v)+')'
    for i in range(1,len(u)-1):
        answer += '(' if u[i] == ')' else ')'
    return answer