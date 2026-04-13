class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c = set()
        c.add(nums[0])
        j = 1
        i = 0
        while i < j and j < len(nums):
            if j-i > k:
                c.remove(nums[i])
                i +=1
            if nums[j] in c:
                return True
            c.add(nums[j])
            j+=1
        return False
            
        