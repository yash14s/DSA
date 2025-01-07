'''
https://leetcode.com/problems/validate-binary-search-tree/

good logic. need to globally check for range
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, min, max):
            if not root:
                return True
            if root.val <= min or root.val >= max:
                return False
            
            return validate(root.left, min, root.val) and validate(root.right, root.val, max)
        return validate(root, -float('inf'), float('inf'))