# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currSum = 0
        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            currSum = l1.val + l2.val + carry
            carry = currSum // 10
            curr.next = ListNode(currSum % 10)
            curr = curr.next 
            currSum = 0
            l1 = l1.next
            l2 = l2.next
        left = None
        if l1:
            left = l1
        if l2:
            left = l2
        while left:
            currSum = left.val + carry
            carry = currSum // 10
            curr.next = ListNode(currSum % 10)
            curr = curr.next 
            currSum = 0
            left = left.next
        if carry != 0:
            curr.next = ListNode(carry)
        
        return dummy.next

        