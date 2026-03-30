class Solution:
    def climbStairs(self, n: int) -> int:
        def steps(n):
            if n == 0:
                return 0
            if n == 1:
                return 1 # because there is 1 way
            if n == 2:
                return 2 # because there are 2 ways
            curr = [1, 2]
            i = 2
            while i < n:
                tmp = curr[0]
                curr[0] = curr[1]
                curr[1] = tmp + curr[1]
                i+=1

            return curr[1]
        return steps(n)
        
        