'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
BFS with a modification
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversed = []
        q = deque()

        if root:
            q.append(root)
        
        level = 0
        while len(q) > 0:
            levelList = []
            
            for _ in range(len(q)):
                node = q.popleft()
                levelList.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level % 2 == 1:
                levelList.reverse()
            
            traversed.append(levelList)
            level += 1
        
        return traversed