class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        curr = 1
        for i in nums:
            prefix.append(curr)
            curr = i*curr
        curr = 1
        for i in range(len(nums)-1,-1, -1):
            suffix.insert(0, curr)
            curr = curr*nums[i]
        
        final = []
        for i in range(len(prefix)):
            final.append(prefix[i]*suffix[i])
        
        return final
            
        