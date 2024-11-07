'''
https://neetcode.io/problems/binary-tree-right-side-view
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        traversed = []
        if not root:
            return traversed

        q = deque()
        q.append(root)

        while len(q) > 0:
            level_nodes = []
            for _ in range(len(q)):
                curr = q.popleft()
                level_nodes.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            visible_node = level_nodes[-1]  #last is right-most
            traversed.append(visible_node)
            
        return traversed
