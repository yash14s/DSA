'''
https://leetcode.com/problems/symmetric-tree/?envType=problem-list-v2&envId=depth-first-search
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymm(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and isSymm(l.left, r.right) and isSymm(l.right, r.left)

        if not root:
            return True
        
        return isSymm(root.left, root.right)
