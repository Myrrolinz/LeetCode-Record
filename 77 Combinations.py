class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.path = []
        self.backtracking(n, k, 1)
        return self.result

    def backtracking(self, n, k, startIdx):
        if len(self.path) == k:
            print(self.path)
            self.result.append(self.path[:])
            return
        for i in range(startIdx, n-(k-len(self.path))+2):
            self.path.append(i)
            self.backtracking(n, k, i+1)
            self.path.pop()