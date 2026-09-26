class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        largest  = 0
        while l < r and r < len(heights):
            if min(heights[l], heights[r])*(r-l) > largest:
                largest = min(heights[l], heights[r])*(r-l)
                if heights[l] > heights[r]:
                    r-=1
                elif heights[r] > heights[l]:
                    l+=1
                else:
                    r-=1
                    l+=1
            else:
                if heights[l] > heights[r]:
                    r-=1
                elif heights[r] > heights[l]:
                    l+=1
                else:
                    r-=1
                    l+=1

        return largest 
                


