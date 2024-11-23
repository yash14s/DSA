'''
https://neetcode.io/problems/matrixBFS
'''

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        def bfs(grid):
            if grid[0][0] == 1:
                return -1

            m, n = len(grid), len(grid[0])
            q = collections.deque()
            visited = set()
            q.append((0,0))
            visited.add((0,0))
            length = 0
            
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    if (r, c) == (m-1, n-1):
                        return length
                    moves = [(1,0), (0,1), (-1,0), (0,-1)]
                    for dr, dc in moves:
                        new_r = r + dr
                        new_c = c + dc
                        if min(new_r, new_c) < 0 or new_r >= m or new_c >= n:
                            continue
                        if grid[new_r][new_c] == 1:
                            continue
                        if (new_r, new_c) in visited:
                            continue
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))
                length += 1
            
            return -1

        return bfs(grid)