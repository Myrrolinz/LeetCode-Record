class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.path = []
        # self.result.append([])
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums, startIdx):
        print(self.path)
        if len(self.path) <= len(nums):
            self.result.append(self.path[:])
            
        if startIdx >= len(nums):
            return

        for i in range(startIdx, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()