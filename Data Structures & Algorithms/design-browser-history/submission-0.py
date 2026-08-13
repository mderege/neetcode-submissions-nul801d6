class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.page = ListNode(homepage)

    def visit(self, url: str) -> None:
        curr = ListNode(url)
        self.page.next = curr
        curr.prev = self.page
        self.page = self.page.next

    def back(self, steps: int) -> str:
        count = 0
        curr = self.page
        while curr.prev and count < steps:
            curr = curr.prev
            count +=1
        self.page = curr
        return curr.val
        

    def forward(self, steps: int) -> str:
        count = 0
        curr = self.page
        while curr.next and count < steps:
            curr = curr.next
            count+=1
        self.page = curr
        return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)