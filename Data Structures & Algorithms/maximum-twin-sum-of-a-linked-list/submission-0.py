# Definition for singly-linked list.

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        curr = slow
        print(slow.val)
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        print(prev.val)
        fast = prev
        slow = head
        maxV = 0
        while fast:
            if fast.val +slow.val > maxV:
                maxV = fast.val+slow.val
            fast = fast.next
            slow = slow.next
        
    
        return maxV
        


        
        
            


        
