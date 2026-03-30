class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNums = {}

        for i in range(len(nums)):
            dictNums[nums[i]] = i
        
        for i in range(len(nums)):
            if (target-nums[i]) in dictNums and  dictNums[(target-nums[i])] != i:
                return [i, dictNums[(target-nums[i])]]

        

        