class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for i in nums:
            sum += i
        if sum%2 != 0:
            return False
        
        def p(i, curr, cache):
            if i >= len(nums):
                return False
            if curr == sum//2:
                return True
            if (i, curr) in cache:
                return cache[(i,curr)]
            withP= False
            without = False
            if curr+ nums[i] < sum//2:
                withP = p(i+1, curr+nums[i], cache)
            if curr+ nums[i] == sum//2:
                return True
            without = p(i+1, curr, cache)

            if withP or without:
                cache[(i, curr)] = True
            else:
                cache[(i, curr)] = False
            return cache[(i, curr)]
        return p(0, 0, {})
            
        