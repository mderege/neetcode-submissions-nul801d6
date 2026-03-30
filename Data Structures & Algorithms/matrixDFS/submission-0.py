class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        def dfs(grid, r, c, visit, ROW, COL):
            if min(r, c) < 0 or r == ROW or c == COL or (r,c) in visit or grid[r][c]==1:
                return 0
            if  r == ROW-1 and c == COL-1 and grid[r][c] == 0:
                return 1 
            
            visit.add((r,c))

            count = 0 
            count += dfs(grid, r+1, c, visit, ROW, COL)
            count += dfs(grid, r-1, c, visit, ROW, COL)
            count += dfs(grid, r, c+1, visit, ROW, COL)
            count += dfs(grid, r, c-1, visit, ROW, COL)

            visit.remove((r,c))
            return count 
            
            

        
        return dfs(grid, 0, 0, set(), ROW, COL)
        