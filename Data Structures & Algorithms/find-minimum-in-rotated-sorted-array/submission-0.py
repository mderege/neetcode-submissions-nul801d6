class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) -1
        output = 0
        if nums[0] >= nums[len(nums)-1]:
            output = nums[len(nums)-1]
            r = len(nums)-1
            l = 1
        else:
            return nums[0]

        while l <= r:
            m= l+((r-l)//2)

            if nums[m] <= output:
                r = m-1
                output = nums[m]
            else:
                l = m+1
                
        
        return output 



        