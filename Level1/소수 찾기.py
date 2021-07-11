def solution(n):
    if n > 3:
        answer = 1
        for i in range(3,n+1,2):
            prime = True
            for j in range(3,int(i**0.5)+1,2):
                if i%j == 0:
                    prime = False
                    break
            if prime:
                answer += 1
        return answer
    else:
        return n-1