class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount = [0]*26
        tCount = [0]*26

        for i in range(len(t)):
            sCount[ord(s[i].lower())-ord('a')] +=1
            tCount[ord(t[i].lower())-ord('a')] +=1

        
        return sCount == tCount