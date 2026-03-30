class Solution:
    def rob(self, nums: List[int]) -> int:
        def steps(nums, n, cache):
            if n < 0:
                return 0
            if n in cache:
                return cache[n]

            total = max(steps(nums, n-2, cache) + nums[n], steps(nums, n-1, cache))
            cache[n] = total
            return cache[n]

        return steps(nums, len(nums)-1, {})


