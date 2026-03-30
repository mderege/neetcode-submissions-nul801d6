class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        ROW, COL = len(grid), len(grid[0])
        def dfs(grid, r, c, visit, ROW, COL):
            if min(r, c) < 0 or r == ROW or c == COL:
                return 0
            if grid[r][c] == '0':
                return 0
            grid[r][c] = '0'

            
            dfs(grid, r+1, c, visit, ROW, COL)
            dfs(grid, r-1, c, visit, ROW, COL)
            dfs(grid, r, c+1, visit, ROW, COL)
            dfs(grid, r, c-1, visit, ROW, COL)
 
            return  
            

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] != '0':
                    island +=1 
                    dfs(grid, i, j, island, ROW, COL) 
        
        return island
