class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left = [1]
        right = [1]*(len(nums)+1)

        for i in range(len(nums)):
            left.append(nums[i]*left[-1])
            right[len(nums)-2- i] = nums[len(nums)-1-i]*right[len(nums)-1-i]
        right = right[:-1]
        left = left[:-1]
        for i in range(len(nums)):
            l = 1
            r = 1
            if i-1 >= 0:
                l = left[i]
            if i+1 < len(nums):
                r = right[i]
            output.append(r*l)
        return output
