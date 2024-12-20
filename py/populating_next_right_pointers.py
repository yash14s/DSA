'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = collections.deque()
        level = []
        if root:
            q.append(root)
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                level.append(node)
            
            for i in range(len(level)):
                if i >= len(level) - 1:
                    level[i].next = None
                else:
                    level[i].next = level[i+1]

        return root