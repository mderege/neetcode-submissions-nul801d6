class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        x = 0
        y = 0
        op = {"+", "-", "/","*"}
        for i in tokens:
            if i not in op:
                nums.append(int(i))
            else:
                y = int(nums.pop())
                x = int(nums.pop())
                if i == "+":
                    res = x+y
                elif i == "*":
                    res = x*y
                elif i == "-":
                    res = x-y
                elif i == "/":
                    res = int(x/y)
                nums.append(res)
            
        return nums[-1]