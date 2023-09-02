bw = ['BWBWBWBW','WBWBWBWB'] * 4
wb = ['WBWBWBWB','BWBWBWBW'] * 4

def black_white(board, x, y):
    cnt = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if board[i][j] != bw[i-x][j-y]:
                cnt+=1
    return cnt
def white_black(board, x, y):
    cnt = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if board[i][j] != wb[i-x][j-y]:
                cnt+=1
    return cnt

n, m = map(int, input().split())
chess = []
result = 64
for i in range(n):
    chess.append(input())
for i in range(n-7):
    for j in range(m-7):
        result = min(result,white_black(chess,i,j))
        result = min(black_white(chess,i,j),result)
print(result)