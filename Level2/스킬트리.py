# 입출력 예
# skill : "CBD"
# skill_trees : ["BACDE", "CBADF", "AECB", "BDA"]
# return : 2

def solution(skill, skill_trees):
    answer = 0

    s_li = list(skill)

    for tree in skill_trees:
        possible = True
        cnt = 0
        for sk in tree:
            if sk in s_li:
                if s_li.index(sk) != cnt:
                    possible = False
                    break
                cnt += 1
        if possible:
            answer += 1

    return answer