# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        re = 0
        result = ListNode()
        curr = result
        while curr1 and curr2:
            tmp = curr1.val +curr2.val +re
            re = 0
            if tmp//10 != 0:
                re = tmp//10
            curr.next = ListNode((tmp%10))
            curr = curr.next
            curr1 = curr1.next
            curr2 = curr2.next
        con = None
        if curr1:
            con = curr1
        if curr2:
            con = curr2
        while con:
            tmp = con.val + re
            re = 0
            if tmp//10 != 0:
                re = tmp//10
            curr.next = ListNode((tmp%10))
            curr = curr.next
            con = con.next
        if re != 0:
            curr.next = ListNode(re)
            
        

        return result.next
        