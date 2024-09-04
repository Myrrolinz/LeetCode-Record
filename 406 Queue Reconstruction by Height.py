class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        que = []

        for p in people:
            que.insert(p[1], p) # 位置，insert的值
        return que