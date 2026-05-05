class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if i >= len(nums):
                return [[]]
            
            perms = helper(i+1)
            result = []
            for z in perms:
                for j in range(len(z)+1):
                    permsC = z.copy()
                    permsC.insert(j, nums[i])
                    result.append(permsC.copy())
            return result
        
        return helper(0)
        