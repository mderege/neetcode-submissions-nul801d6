class ListNode:
    def __init__(self, val: int=None):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        curr = self.head
        
        count = 0
        while curr.next and count < index:
            curr = curr.next
            count +=1
        if count == index:
            return curr.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        curr = ListNode(val)
        curr.next = self.head
        self.head = curr

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        count = 0
        while curr.next and count < index-1:
            curr = curr.next
            count +=1
        if count == index-1:
            tmp = curr.next
            curr.next = ListNode(val)
            curr.next.next = tmp

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        count = 0
        while curr.next and count < index-1:
            curr = curr.next
            count +=1
        if count == index-1 and curr.next:
            curr.next = curr.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)