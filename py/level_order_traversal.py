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

        if not root:
            return traversed

        q = deque()
        q.append(root)

        while len(q) > 0:
            level_nodes = []
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                level_nodes.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            traversed.append(level_nodes)
        
        return traversed
