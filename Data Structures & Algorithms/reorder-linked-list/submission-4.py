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
        slow = head #0
        while slow: 
            curr.next = slow #0
            curr = curr.next #0
            slow = slow.next #1
            curr.next = None
            fast = slow
            while fast and fast.next:
                if fast.next.next == None:
                    curr.next = fast.next
                    curr = curr.next
                    fast.next = None
                else: 
                    fast = fast.next #1
            


        