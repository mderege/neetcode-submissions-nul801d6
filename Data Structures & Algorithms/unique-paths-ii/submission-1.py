class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def paths(grid, v, h, cache):
            if v >= len(grid) or h >= len(grid[0]) or grid[v][h] == 1:
                return 0
            if v == len(grid)-1 and h == len(grid[0])-1:
                return 1
            if (v, h) in cache:
                return cache[(v,h)]
            cache[(v,h)] = paths(grid, v+1, h, cache) + paths(grid, v, h+1, cache)
            return cache[(v,h)]
        
        return paths(obstacleGrid, 0, 0, {})