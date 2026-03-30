class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        if len(self.heap)-k >0:
            tmp = len(self.heap)-k
        else: 
            tmp = 0
        for i in range(tmp):
            heapq.heappop(self.heap)
        self.k = k


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

            
        return self.heap[0]