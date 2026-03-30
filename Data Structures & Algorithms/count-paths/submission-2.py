class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def path(m, n, v, h):
            if v == m-1 and h == n-1:
                return 1
            if v >= m or h >= n:
                return 0
            
            return path(m, n, v, h+1) + path(m, n, v+1, h)
        return path(m,n, 0, 0)