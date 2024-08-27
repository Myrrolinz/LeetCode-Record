# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if not root:
            return result
        self.traversal(root, [], result)
        final_result = []
        for i in result:
            if sum(i) == targetSum:
                final_result.append(i)
        return final_result

    def traversal(self, node, path, result):
        if not node:
            return
        path.append(node.val)
        # targetSum -= node.val
        
        if not node.left and not node.right:
            # 如果是叶子节点且路径和等于目标和，添加到结果
            result.append(list(path))
            # print(result)
        
        # 继续递归遍历左右子树
        if node.left:
            self.traversal(node.left, path, result)
            # 回溯，移除当前节点
            path.pop()
        if node.right:
            self.traversal(node.right, path, result)
            # 回溯，移除当前节点
            path.pop()
        
    
