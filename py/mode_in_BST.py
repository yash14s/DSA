'''
https://leetcode.com/problems/find-mode-in-binary-search-tree/

Inorder traversal to get all values in sorted order. Then add unique counts in a dictionary.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        allNodes = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            allNodes.append(root.val)
            dfs(root.right)
        
        dfs(root)
        counts = {}

        for node in allNodes:
            if node in counts:
                counts[node] += 1
            else:
                counts[node] = 1


        max_freq = max(counts.values())
        
        modes = [key for key, val in counts.items() if val == max_freq]
        
        return modes