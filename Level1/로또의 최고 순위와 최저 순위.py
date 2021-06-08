def solution(lottos, win_nums):
    cnt = 0
    zero = lottos.count(0)

    for i in lottos:
        if win_nums.count(i):
            cnt += 1

    return [abs(cnt + zero - 7) if cnt + zero > 1 else 6, abs(cnt - 7) if cnt > 1 else 6]