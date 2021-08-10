def solution(name):
    asc = []
    for c in name:
        asc.append(min(ord(c)-65,91-ord(c)))
    cur, answer = 0,0
    while True:
        answer += asc[cur]
        asc[cur] = 0
        if sum(asc) == 0:
            break
        left, right = 1,1
        while asc[cur-left] == 0:
            left += 1
        while asc[cur+right] == 0:
            right += 1
        if left < right:
            answer += left
            cur -= left
        else:
            answer += right
            cur += right
    return answer

'''
반례? 'ABBAAAAB' 최솟값은 7? 8?
문제 설명을 읽어보면 마지막 문자에서 커서를 오른쪽으로 이동해서 첫번째로 가는건 불가능!
즉 최솟값은 7이 아닌 8
'''