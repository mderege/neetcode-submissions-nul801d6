class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i != nums.index(nums[i]):
                return nums[i]
        return 0
        