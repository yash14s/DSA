'''
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minDepth = 0
        q = collections.deque()

        if root:
            q.append(root)
        
        while len(q) > 0:
            minDepth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return minDepth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return minDepth