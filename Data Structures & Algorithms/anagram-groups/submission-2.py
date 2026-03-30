class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmpDict = {}
        dictList = []
        for i in strs:
            for j in i:
                tmpDict[j] = 1 + tmpDict.get(j, 0)
            tmp = tmpDict.copy()
            dictList.append(tmp)
            tmpDict.clear()
        tmpAn = []
        final = []
        tmpS = strs.copy()
        for i in range(len(dictList)):
            if strs[i] in tmpS:
                tmpAn.append(strs[i])
                tmpS.remove(strs[i])
                for j in range(len(dictList)):
                    if i != j and dictList[i] == dictList[j]:
                        if strs[j] in tmpS:
                            tmpAn.append(strs[j])
                            tmpS.remove(strs[j])
                            print(tmpS)
                final.append(tmpAn.copy())
            tmpAn.clear()
        print(final)
        return final
                