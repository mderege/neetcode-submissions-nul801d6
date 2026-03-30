class Solution:
    def climbStairs(self, n: int) -> int:
        def steps(n, cache):
            if n == 0:
                return 0
            if n == 1:
                return 1 # because there is 1 way
            if n == 2:
                return 2 # because there are 2 ways
            if n in cache:
                return cache[n]
            cache[n] = steps(n-1, cache) + steps(n-2, cache)

            return cache[n]
        return steps(n, {})
        
        