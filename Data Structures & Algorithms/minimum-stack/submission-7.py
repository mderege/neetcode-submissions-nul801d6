class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val: int) -> None:
        if len(self.stack) > self.size:
            self.stack[self.size] = val
        else:
            self.stack.append(val)
        self.size+=1

    def pop(self) -> None:
        if self.size != 0:
            self.stack[self.size-1] = None
            self.size -=1

    def top(self) -> int:
        return self.stack[self.size-1]

    def getMin(self) -> int:
        print(self.stack)
        minVal = self.stack[0]
        for i in range(self.size):
            if minVal > self.stack[i]:
                minVal = self.stack[i]
        return minVal

            
