from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
            result.append(level)
        return result[::-1]