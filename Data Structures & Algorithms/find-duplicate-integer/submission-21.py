class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[nums[0]]
        slow = nums[0]

        while fast != slow:
            if fast == slow:
                break
            else:
                fast = nums[nums[fast]]
                slow = nums[slow]
        slow2 = 0
        while slow2 != slow:
            if nums[slow] == nums[slow2]:
                return nums[slow]
            slow = nums[slow]
            slow2 = nums[slow2]
                
        return slow
        