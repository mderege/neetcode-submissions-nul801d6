# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head.next
        fast = head.next
        slowest = head

        while fast and fast.next:
            slowest = slowest.next
            slow = slow.next
            fast = fast.next.next
        slowest.next = None
        prev = None 
        curr = slow
        nxt = slow

        while curr:
            nxt = nxt.next
            curr.next = prev
            prev = curr
            curr = nxt

        newL = head
        #2->4->6<-8<-10
        #2,4,6,
        #10, 8
        while prev:
            tmp = newL.next #None
            newL.next = prev #2->10->4->8->6->6
            tmp2 = prev.next #None
            prev.next = tmp # 10->4->8->6->6->None
            prev = tmp2 #None
            newL = tmp # None