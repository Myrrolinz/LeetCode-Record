class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_ = sum(nums)
        if abs(target) > sum_ or (target+sum_)%2 == 1:
            return 0
        target_sum = (target + sum_) // 2
        dp = [0] * (target_sum + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target_sum, num-1, -1):
                dp[i] += dp[i-num]

        return dp[-1]