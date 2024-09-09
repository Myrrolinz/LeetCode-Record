class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [0] * (2*k + 1)
        for i in range(1, 2 * k, 2):
            dp[i] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(1, 2*k + 1):
                if j % 2 == 0:
                    dp[j] = max(dp[j], dp[j-1] + prices[i])
                else:
                    dp[j] = max(dp[j], dp[j-1] - prices[i])
        return dp[2*k]
