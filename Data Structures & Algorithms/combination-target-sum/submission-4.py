class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(i, curr, currSum, subset):
            if currSum == target:
                subset.append(curr.copy())
                return 
            if i >= len(nums) or currSum > target:
                return 
            
            curr.append(nums[i])
            helper(i, curr, currSum+nums[i], subset)
            #helper(i+1, curr, currSum+nums[i], subset)
            curr.pop()

            helper(i+1, curr, currSum, subset)
        
        subset = []
        helper(0, [], 0, subset)
        return subset

        