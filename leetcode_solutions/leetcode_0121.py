class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = prices[0]
        min_price = prices[0]

        result = 0

        for price in prices:
            if price > max_profit:
                max_profit = price
                new_result = max_profit - min_price
                if result < new_result:
                    result = new_result 
            if price < min_price:
                min_price = price
                max_profit = price

        return result