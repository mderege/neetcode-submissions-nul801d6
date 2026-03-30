
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap =  {}
        curr = head
        while curr:
            val = Node(curr.val)
            hashMap[curr] = val
            curr = curr.next
        curr = head
        while curr:
            if curr.next != None:
                hashMap[curr].next = hashMap[curr.next]
            else: 
                hashMap[curr].next = None
            if curr.random != None:
                hashMap[curr].random = hashMap[curr.random]
            else:
                hashMap[curr].random = None
            curr = curr.next
        if head == None:
            return None
        else:
            return hashMap[head]
        