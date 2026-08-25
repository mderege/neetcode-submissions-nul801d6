# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        re = None
        if not head:
            return None
        def helper(curr):
            if curr.next == None:
                nonlocal re
                re = curr
                return curr
            tmp = helper(curr.next)
            curr.next = None
            tmp.next = curr
            tmp = tmp.next
            return tmp
        helper(head)
        return re
            