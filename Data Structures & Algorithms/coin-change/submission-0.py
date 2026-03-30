class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def c(i, cap, cache):
            if cap == 0:
                    return 0
            if i >= len(coins) or cap < 0:
                return float('inf')
            
            
            if (i, cap) in cache:
                return cache[(i, cap)]

            n = c(i+1, cap, cache)
            #if cap - coins[i] >= 0:
            curr = c(i, cap-coins[i], cache)

            if curr != float('inf'):
                curr = curr +1
    
            cache[(i, cap)] = min(curr, n)
            
            return cache[(i,cap)]
        if c(0, amount, {}) == float('inf'):
            return -1
        return c(0, amount, {})
        