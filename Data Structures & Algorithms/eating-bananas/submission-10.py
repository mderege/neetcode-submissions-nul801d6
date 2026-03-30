class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        highestPile = piles[0]
        for i in piles:
            if highestPile < i:
                highestPile = i
        
        l = 1
        r = highestPile
        lowestM = 1
        total = 0
        while l <= r:
            m = l+ ((r-l)//2)
            total = 0
            for i in piles:
                total += math.ceil(i/m)
            
            if total <= h:
                r = m - 1
                lowestM = m
            else:
                l = m + 1
                
            
        return lowestM
            

        