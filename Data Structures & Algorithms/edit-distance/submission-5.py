class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def s(i1, i2,cache):
            if i1 >= len(word1) and i2 >= len(word2):
                return 0
            if i2 >= len(word2) and i1 < len(word1):
                return len(word1) -i1 
            if i1 >= len(word1) and i2 < len(word2):
                return len(word2)-i2
            if (i1,i2) in cache:
                return cache[(i1, i2)]
            if word1[i1] == word2[i2]:
                cache[(i1, i2)] =s(i1+1, i2+1, cache)
            else:
               cache[(i1, i2)] = min(s(i1+1, i2+1, cache), s(i1+1, i2, cache), s(i1, i2+1, cache))+1
            return cache[(i1,i2)]
        return s(0,0, {})