class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adj = {}
        tickets.sort(key = lambda x: x[1])
        # print(f"sorted tickets: {tickets}")
        for u, v in tickets:
            if u in self.adj:
                self.adj[u].append(v)
            else:
                self.adj[u] = [v]
        # print(f"self.adj: {self.adj}")
        self.result = []
        self.dfs("JFK")
        
        return self.result[::-1]

    def dfs(self, s):
        while s in self.adj and len(self.adj[s]) > 0:
            # print(f"now {s}")
            v = self.adj[s][0]
            self.adj[s].pop(0) #pop第一个元素
            self.dfs(v)
        # 只有当当前城市无法继续飞往其他目的地时（即所有从该城市出发的航班都已经用完），才可以确定这个城市是行程的一部分。因此，在确定没有进一步的航班时，才将当前城市加入到 self.result 中。
        self.result.append(s)
        # print(f"self.result:{self.result}")
