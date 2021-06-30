# solution 1
def solution1(n):
    cnt = 1
    while n > 1:
        if n%2 == 1:
            n -= 1
            cnt += 1
        n //= 2
    return cnt

# solution 2
def solution2(n):
    # n을 2진수로 바꾼 뒤 1의 개수를 세면 됨
    return bin(n).count('1')