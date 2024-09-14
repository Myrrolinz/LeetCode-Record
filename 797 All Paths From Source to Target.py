class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        self.path = []
        self.result = []
        self.path.append(0)
        self.dfs(graph, 0, n)
        return self.result

    def dfs(self, graph, x, n):
        print(self.path)
        if x == n-1:
            self.result.append(self.path[:])
            return
        for i in graph[x]:
            self.path.append(i)
            self.dfs(graph, i, n)
            self.path.pop()