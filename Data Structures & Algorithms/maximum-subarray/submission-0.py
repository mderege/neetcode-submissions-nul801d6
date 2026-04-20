class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = -math.inf
        maxSum = -math.inf

        for i in nums:
            currSum = max(currSum, 0) + i
            maxSum = max(maxSum, currSum)
        return maxSum
        