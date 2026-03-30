class Solution:
    def maxArea(self, heights: List[int]) -> int:
        slow = 0
        fast = len(heights)-1
        currLargest = 0

        while slow < fast:
            if (min(heights[fast], heights[slow])*(fast-slow)) > currLargest:
                currLargest = min(heights[fast], heights[slow])*(fast-slow)
            if heights[slow] < heights[fast]:
                slow += 1
            else:
                fast -=1
        # for i in range(len(heights)):
        #     while slow < len(heights) and fast < len(heights):
        #     # if heights[slow] < heights[fast]:
        #     #     slow = fast 
        #     #     fast += 1
        #         print("here is fast", heights[fast])
                # if (min(heights[fast], heights[slow])*(fast-slow)) > currLargest:
                #     currLargest = min(heights[fast], heights[slow])*(fast-slow)
                #     print(currLargest)
                #     fast +=1
        #         else:
        #             fast +=1
        
        #     slow = i
        #     fast = slow+1
            
            

        return currLargest

            
        