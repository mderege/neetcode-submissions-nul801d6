class Solution:
    def search(self, nums: List[int], target: int) -> int:
       high = len(nums)
       low = 0
       curr = len(nums)//2
       if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
       while low < curr and high > curr:
            print(curr)
            if nums[curr] == target:
                return curr
            elif nums[curr] < target:
                low = curr
                curr = (high - curr)//2 + curr
            elif nums[curr] > target:
                high = curr
                curr = (curr)//2 + low
       if nums[curr] == target:
            return curr
       return -1