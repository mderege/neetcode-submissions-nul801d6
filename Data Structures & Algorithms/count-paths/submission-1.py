class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def path(m,n,v, h, cache):
            if v >= m or h >= n:
                return 0
            if (v,h) in cache:
                return cache[(v,h)]
            if v == m-1 and h==n-1:
                return 1

            cache[(v,h)] = path(m, n, v+1, h, cache) + path(m,n, v, h+1, cache)
            return cache[(v,h)]

        return path(m, n, 0, 0, {})