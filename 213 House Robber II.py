class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        result1 = self.robRagne(nums, 0, len(nums) - 2)
        result2 = self.robRagne(nums, 1, len(nums) - 1)
        return max(result1, result2)
    def robRagne(self, nums, start, end):
        if end == start:
            return nums[start]
        prev = nums[start]
        curr = max(nums[start], nums[start + 1])
        for i in range(start + 2, end + 1):
            temp = curr
            curr = max(prev + nums[i], temp)
            prev = temp
        return curr