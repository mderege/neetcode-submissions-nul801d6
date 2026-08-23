# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k ==1:
            return head
        curr = head
        prevEnd = None
        re = None
        while curr:
            count = 1
            currK = curr
            while count < k:
                currK = currK.next
                if currK:
                    count += 1
                if not currK and count < k:
                    if prevEnd:
                        prevEnd.next = curr
                    return re
            if prevEnd:
                prevEnd.next = currK
            prev = None
            currR = curr
            nxt= curr
            tmp = currK.next
            while currR != tmp:
                nxt = nxt.next
                currR.next = prev 
                prev = currR
                currR = nxt
            prevEnd = curr
            if curr == head:
                re = prev
            curr = tmp
        if prevEnd and count == k:
                prevEnd.next = None
        return re
            