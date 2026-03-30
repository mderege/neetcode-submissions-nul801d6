class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = set()
        lenRS = 0
        colSet = set()
        lenCS = 0
        boxes = {0:set(), 1:set(), 2:set(), 3:set(),
        4:set(), 5:set(), 6:set(), 7:set(), 8:set()}
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    lenRS+=1
                    rowSet.add(board[i][j])
                    if lenRS != len(rowSet):
                        return False
                    currLen = len(boxes[(i//3)*3+(j//3)])
                    boxes[(i//3)*3+(j//3)].add(board[i][j])
                    if currLen+1 != len(boxes[(i//3)*3+(j//3)]):
                        return False
                if board[j][i] != ".":
                    lenCS+=1
                    colSet.add(board[j][i])
                    if lenCS != len(colSet):
                        return False
                
            lenRS = 0
            rowSet= set()
            lenCS = 0
            colSet= set()
        

        return True
#1-3x1-3 4-6x1-3 7-9x1-3
#1-3x4-6 4-6x4-6 7-9x4-6
#1-3x7-9 4-6x7-9 7-9x7-9

        