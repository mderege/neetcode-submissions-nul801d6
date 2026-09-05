# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l = 0 
#         r = len(nums)-1

#         while l < r:
#             mid = ((r-l)//2)+l
#             if nums[mid] > nums[r]:
#                 l = mid+1
#             else:
#                 r = mid 

#         if nums[l] == target:
#             return l
#         elif nums[-1] > target and nums[l] < target:
#             r = len(nums)-1
#         else nums[-1] < target and nums[l] < target:
#             r = l-1
#             l = 0

#         while l <=r:
#             mid = ((r-l)//2)+l

#             if nums[mid] > target:
#                 r = mid-1
#             elif nums[mid] < target:
#                 l = mid+1
#             else:
#                 return mid 
#         return -1 




class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        l, r = 0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
        