class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.path = []
        # nums = sorted(nums)
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums, startIdx):
        # print(self.path)
        if len(self.path) > 1:
            self.result.append(self.path[:])
            
        # if startIdx == len(nums):
        #     return

        uset = set()
        for i in range(startIdx, len(nums)):
            if (self.path and nums[i] < self.path[-1]) or nums[i] in uset:
                continue
            uset.add(nums[i])
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()

