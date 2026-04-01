class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        i, j = 0,0 
        while j+i < len(s3):
            if i >= len(s1) and j < len(s2):
                if s2[j] == s3[i+j]:
                    j+=1
                else:
                    return False
            elif i < len(s1) and j >= len(s2):
                if s1[i] == s3[i+j]:
                    i+=1
                else:
                    return False
            else:
                if s2[j] == s3[i+j]:
                    j+=1
                elif s1[i] == s3[i+j]:
                    i+=1
                else:
                    return False
        return True
        # cache = {}
        # def s(i, j, k):
        #     if k >= len(s3):
        #         cache[(i,j,k)] = True
            # if i >= len(s1) and j < len(s2):
            #     if s2[j] == s3[k]:
            #         cache[(i,j,k)] = s(i, j+1, k+1)
            #     else:
            #         cache[(i,j,k)] = False
            # elif i < len(s1) and j >= len(s2):
            #     if s1[i] == s3[k]:
            #         cache[(i,j,k)] = s(i+1, j , k+1)
            #     else:
            #         cache[(i,j,k)] = False
            # else:
            #     if (i,j,k) in cache:
            #         return cache[(i,j,k)]
            #     if s2[j] == s3[k]:
            #         cache[(i,j,k)] = s(i, j+1, k+1)
            #     elif s1[i] == s3[k]:
            #         cache[(i,j,k)] = s(i+1, j , k+1)
            #     else:
            #         cache[(i,j,k)] = False
        #     return cache[(i,j,k)] 
            
        # return s(0,0,0)
            
