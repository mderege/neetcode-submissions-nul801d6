class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currChar = set()
        count = 0
        maxCount = 1
        start = 0
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            currChar.add(s[i])
            if (count+1)!= len(currChar):
                if count > maxCount:
                    maxCount = count
                for j in range(start, i):
                    if s[j] == s[i] and j != i:
                        start = j+1
                        break
                    else:
                        currChar.remove(s[j])
                    print(currChar)
                    
                count = i - start

            count +=1
        
        if count > maxCount:
            maxCount = count
        return maxCount

        