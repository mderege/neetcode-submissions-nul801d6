class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = 0
        r = len(nums)-1
        res = []
        pairs = set()
        for i in range(len(nums)):
            l = 0
            r = i-1
            while l < r:
                curr = (nums[l] + nums[r])
                if (nums[l], nums[r]) not in pairs and curr == nums[i]*(-1):
                    pairs.add((nums[l], nums[r]))
                    res.append([nums[l], nums[i], nums[r]])
                elif curr < nums[i]*-(1):
                    l +=1
                else:
                    r-=1
        return res