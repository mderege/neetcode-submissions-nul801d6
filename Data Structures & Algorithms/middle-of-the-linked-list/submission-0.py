# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        f = head
        s = head
        while f.next:
            f = f.next
            if f.next:
                f = f.next
            
            s = s.next
        
        return s
        