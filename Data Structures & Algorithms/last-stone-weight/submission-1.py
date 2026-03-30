class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)


        while len(stones) > 1:
            print(stones)
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x < y:
                x = x-y
                heapq.heappush(stones, x)
            elif y > x:
                y = y - x
                heapq.heappush(stones, y) 
            else:
                continue 
        if len(stones) == 0:
            return 0
        return -stones[0]




        