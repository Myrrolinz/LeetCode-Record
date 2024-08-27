from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = deque([root])
        while que:
            size = len(que)
            for i in range(size):
                curr = que.popleft()
                if curr:
                    if curr.left:
                        que.append(curr.left)
                    if curr.right:
                        que.append(curr.right)
                    left = curr.left
                    right = curr.right
                    curr.left = right
                    curr.right = left

        return root
                
