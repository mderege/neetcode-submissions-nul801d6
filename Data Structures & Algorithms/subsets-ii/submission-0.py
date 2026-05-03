class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s, h = [], []

        def helper(i, subset, curr):
            if i >= len(nums):
                subset.append(curr.copy())
                return 
            
            curr.append(nums[i])
            helper(i+1, subset, curr)
            curr.pop()

            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            
            helper(i+1, subset, curr)

        helper(0, s, h)
        return s        