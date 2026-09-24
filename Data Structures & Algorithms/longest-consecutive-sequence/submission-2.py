class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr = set(nums)
        longest = 0
        counted = set()
        for i in nums:
            k = i
            count = 1
            if i in counted:
                continue 
            while k+1 in curr:
                count+=1
                counted.add(k)
                k+=1
                
            if count > longest:
                longest = count
        return longest

        