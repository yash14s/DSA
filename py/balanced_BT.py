'''
https://leetcode.com/problems/balanced-binary-tree/?envType=problem-list-v2&envId=depth-first-search
DFS
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0
            leftHeight = helper(root.left)
            if leftHeight == -1:
                return -1
            rightHeight = helper(root.right)
            if rightHeight == -1:
                return -1
            if abs(leftHeight-rightHeight) > 1:
                return -1

            return max(leftHeight, rightHeight) + 1
    
        diff = helper(root)
        return diff != -1