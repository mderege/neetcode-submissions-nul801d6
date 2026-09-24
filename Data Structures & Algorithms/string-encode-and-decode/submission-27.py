class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) +"#"+ i
        return res



    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        print(s)
        while i < len(s):
            t = 0
            while t+i < len(s) and s[i+t] != "#":
                t+=1

            currL = int(s[i:t+i])
            curr = s[i+t+1:i+currL+t+1]
            res.append(curr)
            i += currL+t+1
            print(i)
        return res

        

