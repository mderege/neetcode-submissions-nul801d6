class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        currR = set()
        currC = set()
        for i in range(len(board)):
            currR = set()
            currC = set()
            for j in range(len(board[0])):
                if (board[i][j] != "." and board[i][j] in currR) or (board[j][i] != "." and board[j][i] in currC):
                    return False
                currR.add(board[i][j])
                currC.add(board[j][i])
        box = set()
        for i in range(9):
            box = set()
            pR = (i//3)*3
            pC = (i%3)*3
            for j in range(3):
                for k in range(3):
                    if board[j+pR][k+pC] != "." and board[j+pR][k+pC] in box:
                        return False
                    box.add(board[j+pR][k+pC])
        return True

        
                