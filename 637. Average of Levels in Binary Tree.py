from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        que = deque()
        result = []
        que.append(root)
        while que:
            level = 0
            size = len(que)
            for i in range(size):
                temp = que.popleft()
                level += temp.val
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
            result.append(level / size)
        return result