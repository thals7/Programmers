# DP
def solution(board):
    if len(board) == 1 and len(board[0]) == 1:
        return board[0][0]**2
    answer = 0
    for i in range(1,len(board)):
        for j in range(1,len(board[i])):
            if board[i][j]:
                board[i][j] = min(board[i][j-1],board[i-1][j-1],board[i-1][j])+1
                answer = max(answer,board[i][j])
    return answer**2