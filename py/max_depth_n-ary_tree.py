'''
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        q = collections.deque()
        maxDepth = 0

        if root:
            q.append(root)
        
        while len(q) > 0:
            maxDepth += 1
            for _ in range(len(q)):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
        
        return maxDepth
