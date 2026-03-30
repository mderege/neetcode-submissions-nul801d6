class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def ways(i, curr, cache):
            if curr == amount:
                return 1
            if i >= len(coins):
                return 0
            
            if (i, curr) in cache:
                return cache[(i, curr)]
            way = 0
            if curr+coins[i] < amount:
                way += ways(i, curr+coins[i], cache)
            if curr+coins[i] == amount:
                return 1
            way += ways(i+1, curr,cache)
            cache[(i, curr)] = way

            return cache[(i, curr)]
        return ways(0, 0, {})
        