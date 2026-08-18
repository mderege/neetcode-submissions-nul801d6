
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        existing = {None:None}
        curr = head
        newHead = Node(head.val, head.next, None)
        existing[head] = newHead
        newCurr = newHead
        curr = curr.next
        while curr:
            tmp = Node(curr.val, curr.next, None)
            existing[curr] = tmp
            newCurr.next = tmp
            curr = curr.next
            newCurr = newCurr.next
        
        r2 = newHead
        r2Curr = head

        while r2Curr:
            r2.random = existing[r2Curr.random]
            r2 = r2.next
            r2Curr = r2Curr.next
        return newHead


        