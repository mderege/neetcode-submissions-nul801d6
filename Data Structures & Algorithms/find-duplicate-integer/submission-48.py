class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                curr = 0
                while curr != slow:
                    slow = nums[slow]
                    curr = nums[curr]
                break
        return curr
                