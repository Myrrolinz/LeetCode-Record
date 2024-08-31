class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.path = []
        # self.result.append([])
        nums = sorted(nums)
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums, startIdx):
        print(self.path)
        if len(self.path) <= len(nums):
            self.result.append(self.path[:])
            
        if startIdx >= len(nums):
            return

        for i in range(startIdx, len(nums)):
            if i > startIdx and nums[i] == nums[i-1]:
                continue
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()