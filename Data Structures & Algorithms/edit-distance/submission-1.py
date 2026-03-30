class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def s(i1, i2, w1, cache):
            print(w1)
            print(i1)
            print(i2)
            if i1>= len(w1) and i2 >= len(word2):
                return 0
            if i1< len(w1) and i2 >= len(word2):
                return len(w1)-len(word2)
            elif i1>= len(w1) and i2 < len(word2):
                return len(word2)- len(w1)
            
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            
            if w1[i1] == word2[i2]:
                #if i1+1 < len(w1) and i2+1 < len(word2):
                    cache[(i1, i2)] = s(i1+1, i2+1, w1, cache)
            else:
                cache[(i1, i2)] = min(1+s(i1, i2, w1[:i1]+w1[i1+1:], cache), 1+s(i1, i2+1, w1[:i1]+word2[i2]+w1[i1:], cache), 1+s(i1, i2, w1[:i1]+word2[i2]+w1[i1+1:], cache))
            
            return cache[(i1, i2)]
        return s(0,0, word1, {})