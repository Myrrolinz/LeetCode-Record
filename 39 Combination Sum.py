class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.path = []
        self.backtracking(candidates, target, 0)
        return self.result
    def backtracking(self, candidates, target, startIdx):
        if sum(self.path) >= target:
            if sum(self.path) == target:
                self.result.append(self.path[:])
            return
        i = startIdx
        while sum(self.path) < target and i < len(candidates):
            self.path.append(candidates[i])
            self.backtracking(candidates, target, i)
            i += 1
            self.path.pop()
        startIdx += 1