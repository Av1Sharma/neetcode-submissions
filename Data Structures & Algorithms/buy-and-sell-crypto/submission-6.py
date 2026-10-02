class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max1 = 0
        while sell < len(prices):

            if prices[sell] < prices[buy]:
                buy = sell
            else:
                max1 = max(max1, prices[sell]-prices[buy])
            
            sell +=1

        return max1