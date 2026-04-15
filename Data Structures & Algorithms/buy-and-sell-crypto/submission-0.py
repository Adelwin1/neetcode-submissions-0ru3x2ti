
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_v = float('inf')
        max_profit = 0
        for price in prices:
            if price <min_v:
                min_v= price
            elif price- min_v >max_profit:
                max_profit = price-min_v
        return max_profit