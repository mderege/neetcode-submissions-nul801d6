class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minVal) != 0:
            if self.minVal[-1]  > val:
                self.minVal.append(val)
            else:
                self.minVal.append(self.minVal[-1])
        else:
            self.minVal.append(val)
      

    def pop(self) -> None:
        if len(self.stack) != 0:
            del self.stack[len(self.stack)-1]
        if len(self.minVal) != 0:
            del self.minVal[len(self.minVal)-1]

    def top(self) -> int:
        if len(self.stack) == 0:
            return ""
        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.minVal) > 0:
            return self.minVal[-1]
        else:
            return 0

        
