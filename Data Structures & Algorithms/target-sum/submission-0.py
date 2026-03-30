class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def sum(nums, curSum, i):
            if i >= len(nums) and target == curSum:
                return 1
            if i>=len(nums):
                return 0
            
            ways = sum(nums, curSum+nums[i], i+1) + sum(nums, curSum-nums[i], i+1)

            return ways
        return sum(nums, 0, 0)