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