class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n = len(grid)
        m = len(grid[0])
        self.visited = [[False] * m for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(m):
                # print(grid[i][j])
                # print(self.visited[i][j])
                if grid[i][j] == "1" and not self.visited[i][j]:
                    # print("here")
                    self.visited[i][j] == True
                    res += 1
                    self.dfs(grid, i, j)
        return res
        
    def dfs(self, grid, x, y):
        for i, j in self.directions:
            next_x = x + i
            next_y = y + j
            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                continue
            if not self.visited[next_x][next_y] and grid[next_x][next_y] == "1":
                self.visited[next_x][next_y] = True
                self.dfs(grid, next_x, next_y)