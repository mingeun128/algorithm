class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checkValid = [False] * 10
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if checkValid[int(board[i][j])] == True:
                        return False
                    else:
                        checkValid[int(board[i][j])] = True
            for k in range(len(checkValid)):
                checkValid[k] = False
                
        for i in range(9):
            for j in range(9):
                if board[j][i] != ".":
                    if checkValid[int(board[j][i])] == True:
                        return False
                    else:
                        checkValid[int(board[j][i])] = True
            for k in range(len(checkValid)):
                checkValid[k] = False
                
        for n in [0,3,6]:
            for i in  range(9):
                if i % 3 == 0:
                    for k in range(len(checkValid)):
                        checkValid[k] = False
                for j in range(n,n+3):
                    if board[i][j] != ".":
                        if checkValid[int(board[i][j])] == True:
                            return False
                        else:
                            checkValid[int(board[i][j])] = True
        return True