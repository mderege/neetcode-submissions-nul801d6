class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for i in nums:
            if i not in res:
                res[i] = 0
            res[i] -=1
        r = []
        v = list(res.values())
        heapq.heapify(v)
        i = k
        while i > 1:
            heapq.heappop(v)
            i-=1
        t = heapq.heappop(v)
        for i in res:
            if res[i] <= t:
                r.append(i)
        return r
        