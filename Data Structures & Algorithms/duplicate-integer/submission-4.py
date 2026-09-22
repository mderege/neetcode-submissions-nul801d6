class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = set()

        for i in range(len(nums)):
            vals.add(nums[i])
            if i+1 > len(vals):
                return True
        return False
        
        