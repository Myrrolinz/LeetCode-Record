# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.traversal(0, len(nums), nums)
        return root

    def traversal(self, left, right, nums):
        # max_num = -1
        # max_idx = left
        # for i in range(left, right):
        #     if nums[i] > max_num:
        #         max_num = nums[i]
        #         max_idx = i
        # max_idx = nums.index(max_num)
        # 在 nums[left:right] 范围内找到最大值及其索引
        if left >= right:
            return None
        max_num = max(nums[left:right])
        max_idx = nums.index(max_num, left, right)
        root = TreeNode(max_num)
        root.left = self.traversal(left, max_idx, nums)
        root.right = self.traversal(max_idx+1, right,nums)
        return root