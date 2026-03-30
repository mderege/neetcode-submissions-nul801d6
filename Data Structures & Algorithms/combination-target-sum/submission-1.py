class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        numD = {}
        result = []
        curr = []
        currSum = 0
        
        def main(i, currSum):
            if currSum > target:
                return
            if i >= len(nums):
                return 
            
            if currSum == target:
                result.append(curr.copy())
                return 
            
            currSum += nums[i]
            
            curr.append(nums[i])
            main(i, currSum)

            currSum -= nums[i]
            curr.pop()
            main(i+1, currSum)
        main(0, currSum)
        return result
            
            
            
