def solution(n, words):
    idx = -1
    before = set()
    prev = words[0][0]
    find = False
    for w in words:
        idx += 1
        if w[0] != prev or w in before:
            find = True
            break
        before.add(w)
        prev = w[-1]
    return [idx%n+1,idx//n+1] if find else [0,0]