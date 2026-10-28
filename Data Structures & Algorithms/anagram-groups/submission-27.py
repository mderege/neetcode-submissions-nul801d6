class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i in strs:
            curr = [0]*26
            for j in i:
                curr[ord(j) - ord('a')] +=1
            curr = tuple(curr)
            if curr not in groups:
                groups[curr] = []
            groups[curr].append(i)
            
        return list(groups.values())
