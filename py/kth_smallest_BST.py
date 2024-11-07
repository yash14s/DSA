'''
https://neetcode.io/problems/kth-smallest-integer-in-bst
'''

class Solution:
    def inorder_traversal(self, root):
        if root is None:
            return []
        
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_list = self.inorder_traversal(root)
        return sorted_list[k-1]