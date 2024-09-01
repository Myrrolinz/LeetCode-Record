class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.path = []
        self.backtracking(nums, [False]*len(nums))
        return self.result

    def backtracking(self, nums, used):
        print(self.path)
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return

        for i in range(len(nums)):
            if used[i] == True:
                continue
            used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, used)
            self.path.pop()
            used[i] = False