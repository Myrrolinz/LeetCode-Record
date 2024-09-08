# greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                result += (prices[i] - prices[i-1])
                # print(f"prices[i]:{prices[i]}; result: {result}")

        return result

# dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp0, dp1 = -prices[0], 0
        for i in range(1, length):
            dp1 = max(dp1, dp0 + prices[i])
            dp0 = max(dp0, dp1 - prices[i])
        return dp1