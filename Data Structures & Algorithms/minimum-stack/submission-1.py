class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack == 1:
            self.minVal.append(val)
        else:
            i = 0
            while len(self.minVal) > i and self.minVal[i] < val:\
                i += 1
            self.minVal.insert(i, val)

    def pop(self) -> None:
        if len(self.stack) != 0:
            self.minVal.remove(self.stack[len(self.stack)-1])
            del self.stack[len(self.stack)-1]
        
        

    def top(self) -> int:
        if len(self.stack) == 0:
            return ""
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal[0]

        
