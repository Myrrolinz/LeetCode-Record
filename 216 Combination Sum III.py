class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result = []
        self.path = []
        self.backtracking(n, k, 1)
        return self.result
    def backtracking(self, n, k, startIdx):
        if len(self.path) == k:
            if sum(self.path) == n:
                self.result.append(self.path[:])
            return
        for i in range(startIdx, 10):
            if startIdx >= n:
                return
            self.path.append(i)
            self.backtracking(n, k, i+1)
            self.path.pop()