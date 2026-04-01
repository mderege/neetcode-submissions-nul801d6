class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        def s(i, j, k):
            if k >= len(s3):
                return True
            if i >= len(s1) and j < len(s2):
                if s2[j] == s3[k]:
                    return s(i, j+1, k+1)
                else:
                    return False
            elif i < len(s1) and j >= len(s2):
                if s1[i] == s3[k]:
                    return s(i+1, j , k+1)
                else:
                    return False
            else:
                if s2[j] == s3[k]:
                    return s(i, j+1, k+1)
                elif s1[i] == s3[k]:
                    return s(i+1, j , k+1)
                else:
                    return False

            
        return s(0,0,0)
            
