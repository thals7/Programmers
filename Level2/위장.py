def solution(clothes):
    answer = 1
    closet = {clothes[i][1]:0 for i in range(len(clothes))}
    for i in clothes:
        closet[i[1]] += 1

    for i in closet.values():
        # 해당 종류를 착용하지 않는 경우가 존재하므로 i에 +1 해줌
        answer *= (i+1)

    return answer-1