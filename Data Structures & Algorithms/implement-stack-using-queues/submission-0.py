class MyStack:
    # 1, 2, 3
    # 1, 2
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.c  = 0
    def push(self, x: int) -> None:
        self.q1.append(x)
        self.c+=1

    def pop(self) -> int:
        print(self.q1)
        curr = None
        for i in range(self.c-1):
            curr = self.q1.popleft()
            self.q2.append(curr)
        curr = self.q1.popleft()
        self.q1 = self.q2
        self.q2 = deque()
        self.c -=1
        print(self.q1)
        return curr

    def top(self) -> int:
        curr = None
        print(self.q1)
        for i in range(self.c):
            curr = self.q1.popleft()
            print(curr)
            self.q2.append(curr)
        self.q1 = self.q2
        self.q2 = deque()
        return curr


    def empty(self) -> bool:
        if self.c==0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()