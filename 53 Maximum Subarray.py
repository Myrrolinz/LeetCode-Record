class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        cnt = 0
        for i in range(len(nums)):
            cnt += nums[i]
            if cnt > result:
                result = cnt
            if cnt < 0:
                cnt = 0

        return result
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            result = max(result, dp[i])
        return result