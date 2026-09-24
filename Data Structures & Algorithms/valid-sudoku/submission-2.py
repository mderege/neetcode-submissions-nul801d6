class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            curr = set()
            for j in range(len(board)):
                if board[i][j] != ".":
                    prev = len(curr)
                    curr.add(board[i][j])
                    if len(curr) != prev+1:
                        return False
        for i in range(len(board)):
            curr = set()
            for j in range(len(board)):
                if board[j][i] != ".":
                    prev = len(curr)
                    curr.add(board[j][i])
                    if len(curr) != prev+1:
                        return False
        for k in range(9):
            curr = set()
            r = (k//3)*3
            c = (k%3)*3
            for i in range(3):
                for j in range(3):
                    if board[i+r][j+c] != ".":
                        prev = len(curr)
                        curr.add(board[i+r][j+c])
                        if len(curr) != prev+1:
                            return False
        return True


