class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupA = defaultdict(list)


        for i in strs:
            curr = [0]*26
            for j in i:
                curr[ord(j.lower())-ord('a')] +=1
            curr = tuple(curr)
            # if curr not in groupA:
            #     groupA[curr] = []
            groupA[curr].append(i)

        return list(groupA.values())
        