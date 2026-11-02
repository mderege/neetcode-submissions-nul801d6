class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] +=1
        top = []
        for i in count:
            heapq.heappush(top, (count[i], i))
            while len(top) > k:
                heapq.heappop(top)
        for i in range(len(top)):
            top[i] = top[i][1]
        return top
