class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setSingle = set()
        for i in range(len(nums)):
            setSingle.add(nums[i])
        
        if len(setSingle) != len(nums):
            return True
        else:   
            return False


            
        
         