from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        que = deque()
        result = []
        que.append(root)
        while que:
            level = []
            size = len(que)
            for i in range(size):
                temp = que.popleft()
                level.append(temp.val)
                for child in temp.children:
                    que.append(child)

            result.append(level)
        return result
        