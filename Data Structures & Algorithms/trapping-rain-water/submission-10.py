class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        postfix = []
        currH = height[0]
        totalWater = 0
        for i in range(len(height)):
            if height[i] > currH:
                currH = height[i]
            prefix.append(currH)
        currH = height[-1]
        for i in range(len(height)-1,-1, -1):
            if height[i] > currH:
                currH = height[i]
            postfix.insert(0, currH)
        print(prefix)
        print(postfix)
        for i in range(len(height)):
            print(totalWater)
            totalWater = totalWater + min(prefix[i],postfix[i]) - height[i]
        return totalWater
