# # 2020 카카오 인턴십 문제

def solution(numbers, hand):
    answer = ''
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    L_cur = (3, 0)
    R_cur = (3, 2)
    h = hand.upper()[:1]

    for i in numbers:
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


# 새로운 풀이법 추가
def solution(numbers, hand):
    answer = ''
    nums = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    l,r = (3,0), (3,2)

    for i in numbers:
        if i%3 == 1:
            l = nums[i]
            answer += 'L'
        elif i%3 == 0 and i != 0:
            r = nums[i]
            answer += 'R'

        else:
            lD = abs(nums[i][0]-l[0]) + abs(nums[i][1]-l[1])
            rD = abs(nums[i][0]-r[0]) + abs(nums[i][1]-r[1])

            if lD < rD:
                l = nums[i]
                answer += 'L'
            elif lD > rD:
                r = nums[i]
                answer += 'R'
            else:
                if hand == 'left':
                    l = nums[i]
                    answer += 'L'
                else:
                    r = nums[i]
                    answer += 'R'

    return answer