# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        curr = dummy
        fast = head #0
        mid = 0 
        slow = head #0
        while slow: 
            curr.next = slow #0
            curr = curr.next #0
            slow = slow.next #1
            curr.next = None
            if slow:
                fast = slow.next
            mid = slow
            while mid and fast:
                if fast.next == None:
                    curr.next = fast
                    curr = curr.next
                    if mid:
                        mid.next = None
                fast = fast.next #1
                mid = mid.next
            


        