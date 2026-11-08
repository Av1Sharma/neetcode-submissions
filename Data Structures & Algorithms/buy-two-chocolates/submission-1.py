class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        orgMoney = money
        count = 0
        for i in range(len(prices)):
            if money < prices[i] or count == 2:
                break
            money = money - prices[i]
            count +=1
        if count >=2:
            return money
        else:
            return orgMoney
        
            
        