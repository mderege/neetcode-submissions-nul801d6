class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def seq(text1, text2, i1, i2, cache):
            count = 0
            if i1 >= len(text1) or i2 >= len(text2):
                return 0 
            if (i1, i2) in cache:
                return cache[(i1,i2)]
            if text1[i1] == text2[i2]:
                count += 1
                count += seq(text1, text2, i1+1, i2+1, cache)
                cache[(i1, i2)] = count
            else:
                count += max(seq(text1, text2, i1+1, i2, cache), seq(text1, text2, i1, i2+1, cache))
                cache[(i1, i2)] = count 
            return count
        
        return seq(text1, text2, 0, 0, {})