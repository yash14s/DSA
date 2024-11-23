'''
https://leetcode.com/problems/shortest-path-in-binary-matrix/
Matrix BFS
'''

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        
        q = collections.deque()
        visited = set()

        q.append((0,0))
        visited.add((0,0))
        length = 1

        while q:
            for i in range(len(q)):
                moves = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
                r, c = q.popleft()
                if (r, c) == (m-1, n-1):
                    return length
                for dr, dc in moves:
                    r_ = r + dr
                    c_ = c + dc
                    if min(r_, c_) < 0 or r_ >= m or c_ >= n or grid[r_][c_] == 1 or (r_, c_) in visited:
                        continue
                    q.append((r_, c_))
                    visited.add((r_, c_))
            length += 1
        
        return -1
