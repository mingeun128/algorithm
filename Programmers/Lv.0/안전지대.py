def solution(board):
    answer = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                if i > 0:
                    if board[i-1][j] != 1:
                        board[i-1][j] = 2
                    if j > 0 and board[i-1][j-1] != 1:
                        board[i-1][j-1] = 2
                    if j < n-1 and board[i-1][j+1] != 1:
                        board[i-1][j+1] = 2
                if i < n-1:
                    if board[i+1][j] != 1:
                        board[i+1][j] = 2
                    if j > 0 and board[i+1][j-1] != 1:
                        board[i+1][j-1] = 2
                    if j < n-1 and board[i+1][j+1] != 1:
                        board[i+1][j+1] = 2
                if j < n-1:
                    if board[i][j+1] != 1:
                        board[i][j+1] = 2
                if j > 0:
                    if board[i][j-1] != 1:
                        board[i][j-1] = 2
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer+=1
    return answer