class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def he(i, subset, curr):
            if i >= len(nums):
                subset.append(curr.copy())
                return 
            
            curr.append(nums[i])
            he(i+1, subset, curr)
            curr.pop()

            he(i+1, subset, curr)
            
        s , h = [], []
        he(0, s, h)
        return s