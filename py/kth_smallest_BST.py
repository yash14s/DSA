'''
https://neetcode.io/problems/kth-smallest-integer-in-bst
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversed = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            traversed.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return traversed[k-1]