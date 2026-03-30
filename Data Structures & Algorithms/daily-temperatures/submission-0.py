class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        reversedResult = []

        for i in range(len(temperatures)-1, -1, -1):
            if len(stack) == 0:
                result.append(0)
                stack.append(i)
            else:
                greaterTempFound = False
                while len(stack) != 0 and not greaterTempFound:
                    if temperatures[stack[-1]] > temperatures[i]:
                        greaterTempFound = True
                    else:
                        stack.pop()
                if greaterTempFound:
                    result.append(stack[-1] - i)
                else:
                    result.append(0)
                stack.append(i)
            print(result)

        for j in range(len(result)-1, -1, -1):
            reversedResult.append(result[j])
        return reversedResult