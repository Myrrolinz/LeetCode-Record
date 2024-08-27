# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result = []
        path = []
        if not root:
            return False
        self.traversal(root, path, result)
        print(result)
        if targetSum in result:
            return True
        else:
            return False

    def traversal(self, curr, path, result):
        path.append(curr.val)
        if not curr.left and not curr.right:
            result.append(sum(path))
            return
        if curr.left:
            self.traversal(curr.left, path, result)
            path.pop()
        if curr.right:
            self.traversal(curr.right, path, result)
            path.pop()
            