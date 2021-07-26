def solution(str1, str2):
    j1, j2 = [], []
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            j1.append(str1[i:i + 2].lower())
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            j2.append(str2[i:i + 2].lower())

    if not j1 and not j2: return 65536

    if len(j1) > len(j2):
        inter = [j1.remove(s) for s in j2 if s in j1]
    else:
        inter = [j2.remove(s) for s in j1 if s in j2]
    union = j1 + j2

    return int(len(inter) / len(union) * 65536)