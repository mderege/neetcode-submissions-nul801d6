class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        length = 0
        for i in range(len(s)):

            l= i
            r = i
            curr = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if length < r-l+1:
                    longest = s[l:r+1]
                    length = r-l+1
                l -=1
                r +=1


            
            l = i
            r = i+1
            curr = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if length < r-l+1:
                    longest = s[l:r+1]
                    length = r-l+1
                l -=1
                r +=1
                
                
            
            
        return longest
        