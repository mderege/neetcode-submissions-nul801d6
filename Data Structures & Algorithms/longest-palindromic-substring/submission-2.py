class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        length = 0
        for i in range(len(s)):

            l= i
            r = i
            curr = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if s[l] == s[r]:
                    curr = r-l+1
                l-=1
                r+=1
                
            if length < curr:
                longest = s[l+1:r]
                length = curr
            
            l = i
            r = i+1
            curr = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if s[l] == s[r]:
                    curr = r-l+1
                l -=1
                r +=1
                
            if length < curr:
                longest = s[l+1:r]
                length = curr    
            
            
        return longest
        