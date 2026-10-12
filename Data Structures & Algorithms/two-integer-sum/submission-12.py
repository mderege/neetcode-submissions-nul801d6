class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for i in range(len(nums)):

            if target -nums[i] in differences:
                return [differences[target- nums[i]][0], i]
            differences[nums[i]] = [i]
        
                
        
            
        