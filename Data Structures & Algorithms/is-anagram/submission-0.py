class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tmp = t
        present = False
        curr = 0
        for i in s:
            for j in range(len(tmp)):
                if tmp[j] == i:
                    present = True
                    curr = j
            if not present:
                return False
            else:
                tmp = tmp[:curr] + tmp [curr+1:]
                present = False
            print(tmp)
        return True

