'''
https://leetcode.com/problems/path-sum/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSumRec(self, root, targetSum, path):
        if not root:
            return False
        
        path.append(root.val)
        
        if not root.left and not root.right:
            if targetSum == sum(path):
                return True

        if self.hasPathSumRec(root.left, targetSum, path):
            return True
        if self.hasPathSumRec(root.right, targetSum, path):
            return True
        path.pop()
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasPathSumRec(root, targetSum, [])