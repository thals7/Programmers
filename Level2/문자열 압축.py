def solution(s):
    answer = len(s)

    if len(s) == 1:
        return 1

    # 자르는 문자열의 길이
    for length in range(1, len(s) // 2 + 1):
        # 압축된 최종 문자열
        result = ""
        # 현재 비교 기준이 되는 length 길이의 문자열
        cur = s[:length]
        # 반복된 횟수
        cnt = 1
        # 제일 마지막에 slice 되는 문자열은 length 길이보다 작을수도 있기 때문에 len(s)+length를 해줘서 마지막 문자열까지 for문 돌아갈 수 있게 함
        for i in range(length, len(s)+length, length):
            if s[i:i + length] == cur:
                cnt += 1
            else:
                if cnt == 1:
                    result += cur
                else:
                    result = result + str(cnt) + cur
                cur = s[i:i + length]
                cnt = 1

        answer = min(answer, len(result))

    return answer
