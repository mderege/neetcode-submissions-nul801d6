class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSub = math.inf
        l = 0
        r = 0
        curSum = 0
        minLength = math.inf 
        while l <= r and r < len(nums):
            curSum += nums[r]
            while curSum >= target:
                minLength = min(minLength, r-l+1)
                curSum -= nums[l]
                l +=1  
                      
            r+=1
        
        if minLength < math.inf:
            return minLength
        return 0
