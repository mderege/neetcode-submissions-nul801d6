class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = [0, 0, 0]
        for i in nums:
            colors[i] = colors[i]+1
        
        print(colors)
        k = 0
        for i in range(len(colors)):
            for j in range(colors[i]):
                nums[k] = i
                k+=1
        
        