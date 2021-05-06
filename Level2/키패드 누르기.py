# 2020 카카오 인턴십 문제

def solution(numbers, hand):
    answer = ''
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    L_cur = (3, 0)
    R_cur = (3, 2)
    h = hand.upper()[:1]

    for i in numbers:
        print(L_cur, R_cur)
        print(answer)
        for j in range(4):
            if i == nums[j][0]:
                answer = answer + 'L'
                L_cur = (j, 0)
                break
            elif i == nums[j][2]:
                answer = answer + 'R'
                R_cur = (j, 2)
                break
            elif i == nums[j][1]:
                if abs(j - L_cur[0]) + abs(1 - L_cur[1]) < abs(j - R_cur[0]) + abs(1 - R_cur[1]):
                    answer = answer + 'L'
                    L_cur = (j, 1)
                    break
                elif abs(j - L_cur[0]) + abs(1 - L_cur[1]) > abs(j - R_cur[0]) + abs(1 - R_cur[1]):
                    answer = answer + 'R'
                    R_cur = (j, 1)
                    break
                else:
                    answer = answer + h
                    if h == 'R':
                        R_cur = (j,1)
                    else:
                        L_cur = (j,1)
                    break

    return answer