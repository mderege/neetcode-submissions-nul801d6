class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]]

        for i in range(len(nums)):
            nextPerm = set()
            for j in perms:
                for k in range(len(j)+1):
                    j = list(j)
                    c = j.copy()
                    c.insert(k, nums[i])
                    nextPerm.add(tuple(c.copy()))
            perms= nextPerm.copy()  

        return list(perms)