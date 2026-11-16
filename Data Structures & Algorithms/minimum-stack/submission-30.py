class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVal or self.minVal[-1] >= val:
            self.minVal.append(val)
    
    def pop(self) -> None:
        curr = self.stack.pop(len(self.stack)-1)
        if curr == self.minVal[-1]:
            self.minVal.pop(len(self.minVal)-1)

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        if self.minVal:
            return self.minVal[-1]
        
