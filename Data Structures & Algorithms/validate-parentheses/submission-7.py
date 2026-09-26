class Solution:
    def isValid(self, s: str) -> bool:
        c = []
        matches = {")": "(", "]":"[", "}":"{"}
        for i in s:
            if i == "(" or i == "[" or i == "{":
                c.append(i)
            else:
                if len(c)==0 or c[-1] != matches[i]:
                    return False
                else:
                    c = c[:-1]

        return (len(c) == 0)


        