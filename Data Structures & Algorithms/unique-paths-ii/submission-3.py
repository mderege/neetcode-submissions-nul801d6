class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def path(grid, v, h, cache):
            if v >= len(grid) or h >= len(grid[0]) or grid[v][h] == 1:
                return 0
            if v == len(grid)-1 and h == len(grid[0])-1:
                return 1
            
            
            if (v,h) in cache:
                return cache[(v,h)]
            
            cache[(v,h)] = path(grid, v, h+1, cache) + path(grid, v+1, h, cache)
            return cache[(v,h)]
        return path(obstacleGrid, 0, 0, {})