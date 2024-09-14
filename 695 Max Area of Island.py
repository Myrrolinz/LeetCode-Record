class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n = len(grid)
        m = len(grid[0])
        self.visited = [[False] * m for _ in range(n)]
        self.res = 0
        self.max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not self.visited[i][j]:
                    # print("here")
                    self.visited[i][j] = True
                    self.res = 1
                    self.dfs(grid, i, j)
                    self.max_area = max(self.max_area, self.res)
                elif grid[i][j] == 0:
                    
                    self.visited[i][j] = True
                    self.res = 0
                    print(f"here, {self.res}")
        return self.max_area
        
    def dfs(self, grid, x, y):
        for i, j in self.directions:
            next_x = x + i
            next_y = y + j
            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                continue
            if not self.visited[next_x][next_y] and grid[next_x][next_y] == 1:
                self.visited[next_x][next_y] = True
                self.res += 1
                if self.res > self.max_area:
                    self.max_area = self.res
                print(f"at [{next_x}, {next_y}], area:{self.res}")
                self.dfs(grid, next_x, next_y)