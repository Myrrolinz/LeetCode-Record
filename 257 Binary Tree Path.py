# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getHeight(root) == -1:
            return False
        else:
            return True

    def getHeight(self, node):
        if not node:
            return 0
        leftHeight = self.getHeight(node.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.getHeight(node.right)
        if rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        else:
            return 1 + max(leftHeight, rightHeight)
        # return abs(leftHeight - rightHeight) > 1 ? -1 : 1 + max(leftHeight, rightHeight)
        
        