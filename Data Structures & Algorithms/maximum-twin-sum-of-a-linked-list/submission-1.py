# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 1<-3<-5<-2
        prev = None
        curr = slow
        nxt = slow
        print(curr.val)
        while curr:
            nxt = nxt.next
            curr.next = prev 
            prev = curr
            curr = nxt
            
    
        re = prev.val + head.val
        m = head
        
        while m and prev:
            if m.val +prev.val > re:
                re = m.val+prev.val
            m = m.next 
            prev = prev.next
        return re
        
            
        