class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) != 0:
            del self.stack[len(self.stack)-1]
        

    def top(self) -> int:
        if len(self.stack) == 0:
            return ""
        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return 0
        minVal = self.stack[0]
        for i in self.stack:
            if i < minVal:
                minVal = i
        return minVal

        
