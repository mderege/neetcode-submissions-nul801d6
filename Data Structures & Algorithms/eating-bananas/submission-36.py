class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxH = max(piles)
        def canEat(h, piles, k):
            ck = h
            for i in piles:
                ck-=math.ceil(i/k)
                if ck < 0:
                    return ck
            return ck
        l = 1
        r = maxH
        m = l+(r-l)//2
        while l <= r:
            m = l+(r-l)//2
            c = canEat(h, piles, m)
            if c >= 0:
                r = m-1
            if c < 0:
                l = m+1
            else:
                r = m-1

        return l

        