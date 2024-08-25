# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.cnt_node(root)

    def cnt_node(self, node):
        if not node:
            return 0
        cnt_left = self.cnt_node(node.left)
        cnt_right = self.cnt_node(node.right)
        return cnt_left + cnt_right + 1