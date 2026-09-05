class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = ((r-l)//2)+l

            if nums[mid] > nums[l] and nums[mid] > nums[r]:
                l = mid +1
            elif nums[mid] < nums[l] and nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[l] and nums[mid] < nums[r]:
                r = mid-1
            elif mid == l and nums[mid] < nums[r]:
                return nums[mid] 
            elif mid == l and nums[mid] > nums[r]:
                return nums[r]
            elif mid == l and mid == r:
                return nums[mid]
        return nums[mid]
        