# 2019 카카오 개발자 겨울 인턴십

def solution(board, moves):
    answer = 0
    basket = [0]

    for j in moves:
        for i in range(len(board)):
            if board[i][j-1] == 0:
                continue
            tmp = board[i][j - 1]
            board[i][j-1] = 0
            if tmp == basket[-1]:
                basket.pop()
                answer += 2
                break
            basket.append(tmp)
            break

    return answer