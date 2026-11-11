class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        smallest = float('inf')
        for price in prices:
            profit = max(profit, price - smallest)
            smallest = min(price, smallest)

        return profit
