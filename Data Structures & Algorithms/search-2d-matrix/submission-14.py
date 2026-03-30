class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m*n
        L = 1
        R = t
        #mid = 5-3//2 = 1 x = 0 and y = 1
        #y = 1%4-1 = 1
        #x = 1//4 = 0
        while L<=R:
            mid = ((R-L)//2)+L
            if mid%n == 0:
                x = mid//n -1 
                y = n-1
            else:
                y = mid%n -1
                x= mid//n 

            if matrix[x][y] < target:
                L = mid+1
            elif matrix[x][y] > target:
                R = mid-1
            else:
                return True
        
        return False