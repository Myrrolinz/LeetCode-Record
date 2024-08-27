from collections import Counter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        vec = []
        self.traversal(root, vec)
        mode = float('-inf')
        counts = Counter(vec)
        max_count = max(counts.values())
        # 返回所有出现次数等于最大值的元素
        return [key for key, value in counts.items() if value == max_count]

    def traversal(self, root, vec):
        if root == None:
            return
        self.traversal(root.left, vec)
        vec.append(root.val)
        self.traversal(root.right, vec)