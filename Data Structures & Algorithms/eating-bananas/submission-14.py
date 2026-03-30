import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mo = piles[0]
        for i in piles:
            if mo < i:
                mo = i

        if h > mo and len(piles) == 1:
            return 1

        L = 1
        R = mo

        while L <=R:
            m = ((R-L)//2)+L 
            c = self.kokoCanComplete(piles, h, m)
            if not c:
                L = m+1
            elif c and self.kokoCanComplete(piles, h, m-1):
                R = m-1
            else:
                return m
        return mo
    def kokoCanComplete(self, piles, h, k):
        totalHours = h
        for i in piles:
            if k != 0:
                totalHours = totalHours - math.ceil(i/k)
            if totalHours < 0:
                return False

        return True
        

        