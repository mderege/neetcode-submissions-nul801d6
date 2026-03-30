class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for i in nums:
            sum += i
        if sum%2 != 0:
            return False
        
        def p(nums, i, s, capacity, cache):
            if s == sum//2:
                return True
            if i >= len(nums):
                return False
            if (i,s) in cache:
                return cache[(i, s)]
            c = False
            if nums[i] + s <= capacity:
                c = p(nums, i+1, s+nums[i], capacity, cache)
            m = p(nums, i+1, s, capacity, cache)
            if c or m:
                cache[(i, s)] = True 
            else: 
                cache[(i, s)] = False
            return cache[(i, s)]
        return p(nums, 0, 0, sum//2, {})


        