class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dayToBuy = 0
        dayToSell = 1
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[dayToBuy]:
                dayToBuy = i
            print(profit)
            profit = max(profit, prices[i] - prices[dayToBuy])

        return profit
        