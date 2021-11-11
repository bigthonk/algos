class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            if price < lowest_price :
                lowest_price = price
            profit = price - lowest_price
            if profit > max_profit :
                max_profit = profit
                
        return max_profit
