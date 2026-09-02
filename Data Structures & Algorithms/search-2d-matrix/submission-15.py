class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = ((len(matrix))*(len(matrix[0])))-1

        while l <= r:
            mid = ((r-l)//2)+l
            x = mid//len(matrix[0])
            y = mid % len(matrix[0])

            if matrix[x][y] > target:
                r = mid-1
            elif matrix[x][y] < target:
                l = mid+1
            else:
                return True
        return False