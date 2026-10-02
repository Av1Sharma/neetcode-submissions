class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1

        best = 0


        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if prices[sell] < prices[buy]:
                buy = sell

            sell +=1
            best = max(profit, best)
        return best
        