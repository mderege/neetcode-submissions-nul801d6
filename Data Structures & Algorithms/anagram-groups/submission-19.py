class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDicts = []
        for i in strs:
            dictStr = {}
            for j in i:
                if j in dictStr:
                    dictStr[j] +=1
                else:
                    dictStr[j] = 1
            strDicts.append(dictStr)
            dictStr = {}

        tmpArr = []
        tmpArrDict = []
        final = []
        already = set()
        for j in range(len(strDicts)):
            for i in range(j, len(strDicts)):
                tmp = []
                if len(tmpArr) == 0 or (strDicts[j] == strDicts[i] ):
                    if i not in already:
                        tmpArr.append(strs[i])
                        already.add(i)
                    elif i in already and len(tmpArr) ==0:
                        j = j+1
                print(tmpArr)
                # print("this is j " + strs[j])
                # print("this is i "+strs[i])
            
            if len(tmpArr) != 0:
                final.append(tmpArr)
            tmpArr = []
        return final


            
            


            