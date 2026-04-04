class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 1
        slow = 0

        while fast > slow and fast < len(nums):
            if nums[fast] == nums[slow] and fast != slow:
                return nums[fast]
            else:
                if fast == len(nums)-1:
                    slow +=1
                    fast = slow+1
                else:
                    fast+=1
            
                
        
        