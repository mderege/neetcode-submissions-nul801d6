class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs)):
            result = result + ((str)(len(strs[i])))+"#"+strs[i]
        print(result)
        return result
    def decode(self, s: str) -> List[str]:
        if len(s) != 0:
            curr = s[0]
        length = 0
        i = 1
        result = []
        while i < len(s):
            while s[i].isnumeric():
                curr = curr + s[i]
                i= i+1
            print(curr)
            print(result)
            length = ((int)(curr))
            result.append(s[i+1:i+length+1])
            i = i+length
            i = i+1
            if i+length+2 < len(s):
                curr = s[i+length+2]
            curr = ""
        return result



            
