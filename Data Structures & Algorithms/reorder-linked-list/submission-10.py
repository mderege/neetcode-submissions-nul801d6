# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        #reverse secdond half 
        curr = slow.next
        slow.next = None
        print(slow.val)
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt
        
        #weave new list
        curr2 = prev 
        curr1 = head
        result = ListNode()
        re = result
        while curr1 and curr2:
            nxt1 = curr1.next 
            nxt2 = curr2.next
            curr1.next = curr2
            curr2.next = nxt1
            curr1 = curr1.next.next
            curr2 = nxt2
