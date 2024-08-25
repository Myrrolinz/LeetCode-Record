from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        que = deque()
        # result = []
        que.append(root)
        while que:
            level = []
            size = len(que)
            prev = None
            for i in range(size):
                curr = que.popleft()
                if prev:
                    prev.next = curr
                prev = curr
                # # level.append(temp.val)
                # temp = que.popleft()
                # curr.next = temp
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)

                

            # result.append(level)
        return root