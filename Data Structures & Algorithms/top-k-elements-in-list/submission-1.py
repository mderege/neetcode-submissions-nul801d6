class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmpDict = {}
        for i in nums:
            tmpDict[i] = 1 + tmpDict.get(i, 0)
        result = []
        greatest = -1
        val = -1
        print(tmpDict)
        for i in range(k):
            for j in tmpDict:
                if greatest < tmpDict.get(j, -1):
                    if j not in result:    
                        val = j
                        greatest = tmpDict[j]     
            result.append(val)
            val = -1
            greatest = -1
        return result 
