# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        if head.next == None:
            return head
        
        if head.next.next == None:
            prev = head
            curr = head.next
            curr.next = prev
            prev.next = None
            return curr

        curr = head.next
        prev = head
        prev.next = None
        nextNode = curr.next
        

        while nextNode is not None:
            curr.next = prev
            prev = curr
            curr = nextNode
            nextNode = nextNode.next
        
        curr.next = prev

        return curr



        