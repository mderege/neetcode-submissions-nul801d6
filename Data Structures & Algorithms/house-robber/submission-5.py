class Solution:
    def rob(self, nums: List[int]) -> int:
        def rich(nums, i, cache):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = max(rich(nums, i+1, cache), rich(nums, i+2, cache)+ nums[i])

            return cache[i]
        return rich(nums, 0, {})
    