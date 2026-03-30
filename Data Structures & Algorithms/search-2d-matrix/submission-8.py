class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)*(len(matrix[0]))-1
        if len(matrix) == 1:
            r = len(matrix[0])-1
        while l <= r:
            curr = l + ((r-l)//2)
            m = curr//len(matrix[0])
            n = (curr % len(matrix[0]))
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                r = curr -1
            elif matrix[m][n] < target:
                l = curr +1
        return False


        