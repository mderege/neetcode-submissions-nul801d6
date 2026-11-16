class Solution:
    def isValid(self, s: str) -> bool:
        curr = []
        pairs = {']':'[', '}':'{', ')':'('}
        for i in s:
            if i == '[' or i == '{' or i =='(':
                curr.append(i)
            elif i == ']' or i=='}' or i ==')':
                if not curr:
                    return False
                elif curr[-1] != pairs[i]:
                    return False
                else:
                    curr.pop(len(curr)-1)
        
        if not curr:
            return True
        return False
            