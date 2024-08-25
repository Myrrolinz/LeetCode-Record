# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if left == None and right != None: return False
        elif left != None and right == None: return False
        elif left == None and right == None: return True
        elif left.val != right.val: return False

        val_outside = self.compare(left.left, right.right)
        val_inside = self.compare(left.right, right.left)
        return val_inside and val_outside
        