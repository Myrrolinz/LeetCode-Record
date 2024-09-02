class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        l = 0
        for i in range(len(nums)):
            # print(f"i: {i}; idx: {idx}")
            if i <= idx:
                idx = max(i + nums[i], idx)
            # if idx >= l:
            #     l = idx
            # print(f"now length: {l}")
            if idx >= len(nums)-1:
                return True
        return False
            