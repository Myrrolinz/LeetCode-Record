class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 1. 按绝对值大小排序
        nums.sort(key = lambda x: abs(x), reverse = True)
        # 2. 反转负数
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        # 3. 若k剩余，反复反转最小数
        if k%2 == 1:
            nums[-1] = -nums[-1]
        # 4. 求和
        result = sum(nums)
        return result