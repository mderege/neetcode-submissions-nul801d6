class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum = 0
        for i in stones:
            sum += i
        
        
        def s(stone, i , c, cache):
            if i >= len(stones):
                return abs(c - (sum-c))
            if c >= math.ceil(sum/2):
                return abs(c - (sum-c))
            
            if (i, c) in cache:
                return cache[(i,c)]

            cache[(i, c)] = min(s(stone, i+1 , c+ stone[i], cache), s(stone, i+1 , c, cache) )

            return cache[(i,c)]
        return s(stones, 0, 0, {}) 


        