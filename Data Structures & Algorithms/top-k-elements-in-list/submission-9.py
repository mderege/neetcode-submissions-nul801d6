class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for i in nums:
            if i not in res:
                res[i] = 0
            res[i] +=1
        
        r = [0]*(len(nums)+1)
        for i in res:
            if r[res[i]] == 0:
                r[res[i]] = [i]
            else:
                r[res[i]] += [i]
            #print(r[res[i]])
        top = []
        for i in range(len(r)-1, 0, -1):
            if len(top) == k:
                return top
            if r[i] != 0:
                top += r[i]
        return top
            



        