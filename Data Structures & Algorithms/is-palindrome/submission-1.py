class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        # for i in range(len(s)):
        #     if s[i] != s[len(s)-1-i]:
        #         return False
        i = 0 
        j = len(s)-1
        while i < len(s):
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    print(s[i])
                    print(s[j])
                    return False
                i+=1
                j-=1
            if i < len(s):
                if not (s[i].isalnum()):
                    i +=1
                if not (s[j].isalnum()):
                    j -= 1        
            

        return True


        