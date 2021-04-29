def solution(n):

    ans_li = []
    numbers = ['4','1','2']

    while n:
        ans_li.insert(0,numbers[n%3])
        if n % 3 == 0:
            n = n//3 -1
        else:
            n = n//3

    answer = ''.join(ans_li)

    return answer