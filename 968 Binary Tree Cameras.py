# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result = [0] # 这是为了能在函数中修改并返回，如果只是整数，那就是传值（不可变），而不是传引用。
        # 根节点没覆盖所以要+1
        if self.traversal(root, result) == 0:
            result[0] += 1
        return result[0]

    # 0：该节点无覆盖
    # 1：本节点有摄像头
    # 2：本节点有覆盖
    def traversal(self, cur, result):
        if not cur:
            return 2
        left = self.traversal(cur.left, result)
        right = self.traversal(cur.right, result)

        # 如果左右节点都有覆盖，则父节点无覆盖
        if left == 2 and right == 2:
            return 0
        # 如果左右节点存在无覆盖，则本节点要安装摄像头
        if left == 0 or right == 0:
            result[0] += 1
            return 1
        # 如果左右节点存在摄像头，则本节点被覆盖
        if left == 1 or right == 1:
            return 2
            
