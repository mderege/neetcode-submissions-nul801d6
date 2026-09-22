class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # s = []
        # result = []
        # for i in strs:
        #     curr = {}
        #     for j in i:
        #         if j not in curr:
        #             curr[j] = 0
        #         curr[j] +=1
            
        #     s.append([curr, i])
        # used = set()
        # for i in range(len(s)):
        #     if s[i][1] in used:
        #         continue
        #     c = [s[i][1]]
        #     for j in range(i+1, len(s)):
        #         if s[i][0] == s[j][0]:
        #             c.append(s[j][1])
        #             used.add(s[j][1])
        #     result.append(c)

        # return result

        
        curr = {}
        for i in strs:
            counts = [0]*26
            for j in i:
                counts[ord(j) - ord('a')] +=1
            
            if tuple(counts) not in curr:
                curr[tuple(counts)] = []
            curr[tuple(counts)] += [i]
            
        return list(curr.values())

            
        




        

        

