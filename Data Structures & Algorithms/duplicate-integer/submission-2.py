class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsD = {}

        for i in nums:
            if i in numsD:
                return True
            else:
                numsD[i] = 1
        return False