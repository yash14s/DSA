'''
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
This is Brute Force solution
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        visited = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            visited.append(root.val)
            dfs(root.right)
        dfs(root)
        visited.sort()
        smallest = visited[0]
        for val in visited:
            if val > smallest:
                return val
        return -1
