# 210806
def solution(w,h):
    a,b = max(w,h),min(w,h)
    while b != 0:
        print(a,b)
        a = a % b
        if a == 0:
            break
        a,b = b,a
    return w*h-(b*(w//b+h//b-1))

# 최대공약수 구하기
def gcd(a,b):
    if a == 0:
        return b
    else:
        gcd(b%a,a)