class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceP = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = x**2 + y**2
            distanceP.append((dist, [x,y]))
        
        heapq.heapify(distanceP)

        res = []

        for i in range(k):
            res.append(heapq.heappop(distanceP)[1])

        return res