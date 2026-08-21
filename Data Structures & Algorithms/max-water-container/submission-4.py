class Solution:
    def maxArea(self, heights: List[int]) -> int:
        slow = 0
        fast = len(heights)-1
        currLargest = 0
        theSlow = 0
        theFast = 0
        while slow < fast:
            if (min(heights[fast], heights[slow])*(fast-slow)) > currLargest:
                currLargest = min(heights[fast], heights[slow])*(fast-slow)
                theSlow = slow
                theFast = fast
            if heights[slow] < heights[fast]:
                slow += 1
            else:
                fast -=1
        
        
        print(theFast)
        print(theSlow)
            

        return currLargest

            
        