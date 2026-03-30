class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow = len(prices)-1
        fast = len(prices)-2
        highest = prices[slow] - prices[fast] 
        for i in range(len(prices)-1, -1, -1):
            if prices[slow] < prices[i]:
                slow = i
            elif prices[slow] - prices[i] > highest:
                highest = prices[slow] - prices[i]
        
        if highest < 0:
            return 0
        return highest

