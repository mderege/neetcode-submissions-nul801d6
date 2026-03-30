class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = len(nums)//2
        L = 0
        R = len(nums)
        while L <= R and m < len(nums):
            if nums[m] == target:
                return m
            elif nums[m] > target:
                R = m-1
            else:
                L = m+1
            m = ((R-L)//2)+L

        return -1
    
             


        