from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = deque()
        cnt = 0
        que.append(root)
        while que:
            size = len(que)
            for i in range(size):
                temp = que.popleft()
                # level.append(temp.val)
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
            cnt += 1
        return cnt