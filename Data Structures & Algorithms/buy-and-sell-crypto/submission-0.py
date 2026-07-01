class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = prices[0]
        max_score = 0
        for index in range(1, len(prices)):
            if prices[index] <= left:
                left = prices[index]
            else:
                max_score = max(max_score, prices[index] - left)
        return max_score