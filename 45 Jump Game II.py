class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        idx = 0
        ans = 0
        curr_dist = 0
        for i in range(len(nums)):
            idx = max(i + nums[i], idx)
            if i == curr_dist:
                ans += 1
                curr_dist = idx
                if idx >= len(nums)-1:
                    break
        return ans