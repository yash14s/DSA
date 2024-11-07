'''

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Doubt was how to use add visited nodes to a list. I didn't know how to init the list, so I used two functions. This solution works too. But I wanted an elegant solution that uses a single function. That solutiin is the uncommented one.
    def inorder_recursive(self, root, res=[]):
        if root is None:
            return []
        
        self.inorder_recursive(root.left, res)
        res.append(root.val)
        self.inorder_recursive(root.right, res)
        
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder_recursive(root, [])
    '''

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Base case: if the node is None, return an empty list
        if root is None:
            return []
        
        # Recursive case: combine left, root, and right values in an inorder sequence
        return (
            self.inorderTraversal(root.left) +  # Left subtree
            [root.val] +                        # Root value
            self.inorderTraversal(root.right)   # Right subtree
        )
