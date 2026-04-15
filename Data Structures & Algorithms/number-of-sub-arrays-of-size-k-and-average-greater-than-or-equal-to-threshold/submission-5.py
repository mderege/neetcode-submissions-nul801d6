class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        avg = 0
        i = 0
        j = k
        for m in range(0, k):
            avg += arr[m]
        if avg/k >= threshold:
           count+=1
        while i < j and j < len(arr):
            avg = avg - arr[i]
            avg += arr[j]
            i+=1      
            # if avg/k >= threshold and j-i == k:
            #     count+=1
            
            j +=1
            if avg >= threshold*k and j-i ==k:
                count +=1
            
        
            # print(avg)
            
        return count