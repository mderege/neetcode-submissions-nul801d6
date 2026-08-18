# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None 
        curr = slow
        nxt = slow

        while curr:
            nxt = nxt.next
            curr.next = prev
            prev = curr
            curr = nxt

        newL = head
        print(prev.val)
        #2,4,6,8
        #2,4,6,
        #10, 8
        while prev and newL and newL.next:
            tmp = newL.next #6
            newL.next = prev #2->10
            tmp2 = prev.next #8
            prev.next = tmp # 2->10-4
            prev = tmp2 #8
            newL = newL.next.next # 4
            if not prev:
                newL.next = None
                break
        