'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Using BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        q = collections.deque()

        if root:
            q.append(root)
        
        while len(q) > 0:
            maxDepth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return maxDepth
    '''
    #Using DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1