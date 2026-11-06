class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr = 0
        maxC = 0
        i = 0
        num = set(nums)
        checked = set()
        while i < len(nums):
            c = nums[i]
            if c in checked:
                i+=1
                continue
            curr+=1
            while i >= 0 and c-1 in num:
                curr +=1
                checked.add(c-1)
                c-=1
            i+=1
            maxC = max(maxC, curr)
            curr = 0
            

            
        return maxC