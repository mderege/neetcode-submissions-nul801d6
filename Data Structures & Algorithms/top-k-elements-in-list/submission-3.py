class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for i in nums:
            if i not in res:
                res[i] = [0, i]
            res[i][0] -=1
        r = []
        v = list(res.values())
        heapq.heapify(v)
        i = k
        while i > 0:
            r.append(heapq.heappop(v)[1])
            i-=1

        return r
        