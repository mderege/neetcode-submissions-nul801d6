class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}

        for i in range(len(nums)):
            if target - nums[i] in n:
                return [n[target - nums[i]], i]
            else:
                n[nums[i]] = i