class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1

        while l < r:
            mid = ((r-l)//2)+l
            if nums[mid] == target:
                return mid
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid 
        print(nums[l])
        print(nums[r])
        if nums[l] == target:
            return l
        elif nums[-1] > target:
            r = len(nums)-1
        elif nums[-1] < target:
            r = l 
            l = 0

        while l <=r:
            mid = ((r-l)//2)+l

            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid 
        return -1 
        