class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        island = set()
        ROW, COL = len(grid), len(grid[0])
        def dfs(grid, r, c, curr , ROW, COL):
            if min(r, c) < 0 or r == ROW or c == COL:
                return 0
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            visit = 1

            
            visit += dfs(grid, r+1, c, visit, ROW, COL)
            visit += dfs(grid, r-1, c, visit, ROW, COL)
            visit += dfs(grid, r, c+1, visit, ROW, COL)
            visit += dfs(grid, r, c-1, visit, ROW, COL)
 
            return  visit
        
        maxArea = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] != 0:
                    area = 0
                    area = dfs(grid, i, j, area, ROW, COL) 
                    if area > maxArea:
                        maxArea = area
        
        return maxArea