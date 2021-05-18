# 첫번째 풀이
def solution(N, stages):
    stage = {i: 0 for i in range(1, N + 1)}
    cur = {i: 0 for i in range(1, N + 1)}
    fail = {i: 0 for i in range(1, N + 1)}

    for user in stages:
        if user == N+1:
            for i in range(1,user):
                stage[i] += 1
        else:
            cur[user] += 1
            for i in range(1, user + 1):
                stage[i] += 1

    for i in range(1, N + 1):
        if cur[i] == 0:
            fail[i] = 0
        else:
            fail[i] = float(cur[i]) / float(stage[i])
    print(fail)
    answer = sorted(fail, key=lambda x: fail[x], reverse=True)

    return answer


# 다른 풀이 참고
def solution(N,stages):
    answer = {}
    users = len(stages)

    # 1단계는 모든 user가 풀었거나 풀고있는 중이므로 한단계 올라갈 때마다 현재 스테이지에 머물러있는 cnt 수를 user에서 빼주면 됨
    for stage in range(1,N+1):
        if users == 0:
            answer[stage] = 0
        else:
            cnt = stages.count(stage)
            answer[stage] = cnt / users
            users -= cnt

    answer = sorted(answer, key=lambda x:answer[x], reverse=True)

    return answer