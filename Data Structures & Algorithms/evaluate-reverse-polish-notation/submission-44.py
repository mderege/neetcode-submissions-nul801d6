class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {'+', '-', '*', "/"}
        curr = []
        for i in tokens:
            if i in operands:
                op2 = int(curr.pop(len(curr)-1))
                op1 = int(curr.pop(len(curr)-1))
                if i == '+':
                    curr.append(op1+op2)
                elif i == '-':
                    curr.append(op1-op2)
                elif i == '/':
                    curr.append(int(op1/op2))
                elif i == '*':
                    curr.append(op1*op2)
            else:
                curr.append(int(i))
                
        return curr[-1]

