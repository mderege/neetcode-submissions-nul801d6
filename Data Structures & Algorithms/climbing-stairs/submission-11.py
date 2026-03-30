class Solution:
    def climbStairs(self, n: int) -> int:
        if n <2:
            return 1
        curr = [1, 2]
        i = 2
        while n > i:
            tmp = curr[1]
            curr[1] = curr[0] +curr[1]
            curr[0] = tmp
            i +=1
        return curr[1]