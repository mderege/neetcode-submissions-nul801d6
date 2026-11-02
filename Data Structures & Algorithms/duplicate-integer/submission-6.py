class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set()

        for i in range(len(nums)):
            d.add(nums[i])
            if len(d) != i+1:
                return True
        return False