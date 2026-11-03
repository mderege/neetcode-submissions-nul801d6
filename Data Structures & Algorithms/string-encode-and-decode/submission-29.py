class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for i in strs:
            r += str(len(i)) + "#"+i
        print(r)
        return r

    def decode(self, s: str) -> List[str]:
        i = 0
        prev = 0
        r = []
        while i < len(s):
            while s[i] != "#":
                i +=1
            curr = int(s[prev:i])+i
            r.append(s[i+1:curr+1])
            prev = curr+1
            i = prev
        print(r)
        return r

            


