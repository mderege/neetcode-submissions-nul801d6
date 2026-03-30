class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        if len(tokens) < 3:
            return 0
        stack.append(tokens[0])
        stack.append(tokens[1])

        i = 2

        while len(stack) > 0 and i < len(tokens):
            if tokens[i] == '+':
                first = stack.pop()
                second = stack.pop()
                stack.append(int(first) + int(second))
            elif tokens[i] == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) - int(second))
            elif tokens[i] == '*':
                first = stack.pop()
                second = stack.pop()
                stack.append(int(first) * int(second))
            elif tokens[i] == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(int(first) / int(second)))
            else:
                stack.append(tokens[i])
            i +=1
            print(stack)

        return stack[0]
