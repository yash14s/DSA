'''
https://leetcode.com/problems/path-sum-ii/description/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, paths, path):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                if sum(path) == targetSum:
                    paths.append(path[:])
            
            dfs(root.left, paths, path)
            dfs(root.right, paths, path)
            path.pop()
            
        paths = []
        dfs(root, paths, [])
        return paths
