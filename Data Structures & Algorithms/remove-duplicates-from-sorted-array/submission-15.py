class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        #ordering of if statements 
        while l < r and r < len(nums):
            if nums[l] == nums[r]:
                r = r+1
            elif l+1 < r:
                nums[l+1] = nums[r]
                l = l+1
            else:
                l = l+1
                r = r+1
        nums = nums[:l+1]
        
        return len(nums)       