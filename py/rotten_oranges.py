'''
https://leetcode.com/problems/rotting-oranges/
Matrix BFS
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()

        numFresh = 0
        numRotten = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    numFresh += 1
                if grid[r][c] == 2:
                    numRotten += 1
                    q.append((r,c))
                    visited.add((r,c))
        
        if numFresh == 0:
            return 0
        if numRotten == 0:
            return -1
        
        minutes = 0

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if grid[r][c] == 1:
                    numFresh -= 1
                if numFresh == 0:
                    return minutes
                moves = [(1,0), (0,1), (-1,0), (0,-1)]
                for dr, dc in moves:
                    r_ = r + dr
                    c_ = c + dc
                    if min(r_, c_) < 0 or r_ >= m or c_ >= n or grid[r_][c_] == 0 or (r_, c_) in visited:
                        continue
                    q.append((r_, c_))
                    visited.add((r_, c_))
            minutes += 1

        return -1