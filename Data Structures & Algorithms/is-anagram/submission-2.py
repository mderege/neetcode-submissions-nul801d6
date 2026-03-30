class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}

        for i in s:
            if i in dictS:
                dictS[i] +=1
            else:
                dictS[i] = 1
        for j in t:
            if j in dictT:
                dictT[j] +=1
            else: 
                dictT[j] = 1
        longest = {}
        shortest = {}
        if len(dictS) > len(dictT):
            longest = dictS
            shortest = dictT
        else:
            longest = dictT
            shortest = dictS
        for i in longest:
            if i in shortest:
                if longest[i] != shortest[i]:
                    return False
            else:
                return False

        return True

        