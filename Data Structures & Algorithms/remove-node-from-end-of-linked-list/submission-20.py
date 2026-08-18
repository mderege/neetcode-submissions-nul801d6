# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 1
        if not head.next:
            return None
        while curr and count <= n:
            count+=1
            curr = curr.next
        slow = head
        if not curr:
            return head.next
        while curr and curr.next:
            slow = slow.next
            curr = curr.next
        print(slow.val)
        slow.next = slow.next.next
        return head
        

        