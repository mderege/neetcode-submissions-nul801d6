class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = (len(matrix)*(len(matrix[0])))-1

        while l <= r:
            m = ((r-l)//2)+l 
            x = m//(len(matrix[0]))
            y = m%(len(matrix[0]))
            if matrix[x][y] > target:
                r = m-1
            elif matrix [x][y] < target:
                l = m+1
            else:
                return True
        return False

        