class Solution:
    def climbStairs(self, n: int) -> int:
        return self.main(n, {})
    def main(self, n, cache):
        if n == 0:
            return 0
        if n in cache:
            total = cache[n]
        elif n == 1:
            return 1
            cache[n] = 1
        elif n==2:
            return 2
            cache[n] = 2
        else:
            total = self.main(n-1, cache) + self.main(n-2, cache)
            cache[n] = total
        return total 

        
        

        