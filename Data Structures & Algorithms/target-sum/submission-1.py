class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def sum(nums, curSum, i, cache):
            if i >= len(nums) and target == curSum:
                return 1
            if i>=len(nums):
                return 0
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            
            cache[(i, curSum)] = sum(nums, curSum+nums[i], i+1, cache) + sum(nums, curSum-nums[i], i+1, cache)

            return cache[(i, curSum)]
        return sum(nums, 0, 0, {})