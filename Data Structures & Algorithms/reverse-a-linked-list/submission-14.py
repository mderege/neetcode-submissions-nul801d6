#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1->2->3->4->5
        if head == None or head.next == None:
            return head
        nextV = head.next #2
        curr = head#1
        curr.next = None 
        end = None
        while nextV != None:
            tmp = nextV.next 
            nextV.next = curr
            end = nextV
            curr = nextV 
            nextV = tmp 
        return end
