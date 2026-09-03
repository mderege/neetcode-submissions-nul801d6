class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        lower = True
        mid = ((r-l)//2)+l
        n = math.inf
        if len(piles) == h:
            return max(piles)
        while l <= r:
            mid = ((r-l)//2)+l
            curr = h 

            for i in piles:
                curr -= math.ceil(i/mid)

            if curr >= 0:
                r = mid-1
                #n = min(n, mid)
            elif curr < 0:
                l = mid+1
                #n = min(n, mid)

        return l
        