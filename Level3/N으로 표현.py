def solution(N,number):
    if N == number:
        return 1
    lst = [set() for _ in range(8)]
    for i,s in enumerate(lst, start=1):
        s.add(int(str(N)*i))

    for i in range(1,8):
        for j in range(i//2+1):
            for x in lst[j]:
                for y in lst[i-j-1]:
                    lst[i].add(x+y)
                    lst[i].add(x-y)
                    lst[i].add(x*y)
                    if x != 0:
                        lst[i].add(y//x)
        if number in lst[i]:
            return i+1
    return -1
