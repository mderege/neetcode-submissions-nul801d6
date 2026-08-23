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
        currK = None
        re = None
        while curr:
            count = 1
            currK = curr
            while count < k:
                currK = currK.next
                if currK:
                    count += 1
                if not currK and count < k:
                    currK = curr
                    #print("here")
                    break
            #print(currK.val)
            #print(count)
            if count != k:
                if prevEnd:
                    prevEnd.next = currK
                #print(prevEnd.next.val)
                break
            if prevEnd:
                prevEnd.next = currK
                #print(prevEnd.next.val)
            prev = None
            currR = curr
            nxt= curr
            tmp = currK.next
            while currR:
                nxt = nxt.next
                currR.next = prev 
                prev = currR
                currR = nxt
                if currR == currK:
                    currR.next = prev 
                    prev = currR
                    #currR = nxt
                    break
            prevEnd = curr
            if curr == head:
                re = prev
            #print(curr.val)
            curr = tmp
        if prevEnd and currK == currR:
                prevEnd.next = None
        return re
            