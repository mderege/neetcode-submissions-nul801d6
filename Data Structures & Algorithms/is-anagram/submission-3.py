class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetters = {}
        tLetters = {}

        for i in s:
            if i not in sLetters:
                sLetters[i] = 0
            sLetters[i] +=1
        for i in t:
            if i not in tLetters:
                tLetters[i] = 0
            tLetters[i] +=1
        
        if sLetters == tLetters:
            return True
        return False
        
