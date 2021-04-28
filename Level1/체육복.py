def solution(n, lost, reserve):
    answer = n - len(lost)

    # for문에서 리스트의 원본을 돌릴 경우 리스트의 요소를 remove하면 원본 리스트 데이터가 훼손되기 때문에 누락이 발생
    # 따라서 list[:] 라는 리스트의 복사본을 만들어 이를 루프에 넣고 돌리면 누락이 일어나지 않음
    for i in reserve[:]:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
            answer += 1

    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
            answer += 1
        elif i + 1 in lost:
            lost.remove(i + 1)
            answer += 1

    return answer