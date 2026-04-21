class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currSum = math.inf
        maxSum = -math.inf
        minSum = math.inf
        total = 0

        for i in nums:
            currSum = min(currSum, 0)+i
            minSum = min(currSum, minSum)

        for i in nums:
            total +=i
        
        currSum = -math.inf
        
        for i in nums:
            currSum = max(currSum, 0) + i
            maxSum = max(currSum, maxSum)
        
        if total-minSum ==0:
            return maxSum
        
        return max(maxSum, total-minSum)

        