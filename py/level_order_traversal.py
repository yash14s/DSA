'''
https://neetcode.io/problems/level-order-traversal-of-binary-tree
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversed = []
        q = collections.deque()

        if root:
            q.append(root)
        
        while len(q) > 0:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            traversed.append(level)
        
        return traversed
        
