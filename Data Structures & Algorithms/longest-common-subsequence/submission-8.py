class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def s(i1, i2, cache):
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            
            if (i1, i2) in cache:
                return cache[(i1,i2)]
            
            if text1[i1] == text2[i2]:
                cache[(i1, i2)] = 1+s(i1+1, i2+1, cache)
            else:
                cache[(i1, i2)] = max(s(i1+1, i2, cache), s(i1, i2+1, cache))
            
            return cache[(i1, i2)]
        
        return s(0,0, {})
        