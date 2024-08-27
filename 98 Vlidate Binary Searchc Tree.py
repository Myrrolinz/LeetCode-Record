# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        vec = []
        self.traversal(root, vec)
        for i in range(len(vec) - 1):
            if vec[i] >= vec[i+1]:
                return False
        return True

    def traversal(self, root, vec):
        if root == None:
            return
        self.traversal(root.left, vec)
        vec.append(root.val)
        self.traversal(root.right, vec)