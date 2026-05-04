class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for p_start in range(len(prices)):
            for p_end in range(p_start, len(prices)):
                if prices[p_end] - prices[p_start] > profit:
                    profit = prices[p_end] - prices[p_start]
        return profit