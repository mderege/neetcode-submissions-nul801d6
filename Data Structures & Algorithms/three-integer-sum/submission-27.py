class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        

        for i, a in enumerate(nums):
            l = i+1
            r = len(nums)-1
            if i > 0 and a == nums[i-1]:
                continue
            while l < r:
                if nums[l] + nums[r]+a < 0:
                    l +=1
                elif nums[l]+ nums[r] +a > 0:
                    r-=1
                elif nums[l]+ nums[r] +a == 0:
                    res.append([nums[l], nums[r], a])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    r-=1

        return res
