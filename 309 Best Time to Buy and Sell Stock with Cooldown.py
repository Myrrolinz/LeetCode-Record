class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        dp = [0] * 4  # 4 states: hold, cooldown, sell, cooldown-after-sell
        dp[0] = -prices[0]
        
        for i in range(1, n):
            prev_dp = dp[:]  # Create a copy of the previous day's states
            
            dp[0] = max(prev_dp[0], max(prev_dp[3], prev_dp[1]) - prices[i])  # holding stock
            dp[1] = max(prev_dp[1], prev_dp[3])  # in cooldown, cannot buy
            dp[2] = prev_dp[0] + prices[i]  # sell today
            dp[3] = prev_dp[2]  # cooldown after selling
            
            # Debug print for understanding state transitions
            print(f"0: {dp[0]}; 1: {dp[1]}; 2: {dp[2]}; 3: {dp[3]};")

        # Return the max profit of the last day when not holding stock
        return max(dp[1], dp[2], dp[3])