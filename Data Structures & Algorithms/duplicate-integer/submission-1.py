class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictNums = {}
        for i in nums:
            if i in dictNums:
                dictNums[i] += 1
                return True
            else:
                dictNums[i] = 1
        return False
        