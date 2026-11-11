class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        smallest = float('inf')
        for price in prices:
            smallest = min(price, smallest)
            profit = max(profit, price - smallest)

        return profit
