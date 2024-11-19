'''
https://leetcode.com/problems/max-area-of-island/?source=submission-ac
Matrix DFS
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c, visited):
            if min(r,c) < 0 or r >= m or c >= n:
                return
            if grid[r][c] == 0:
                return
            if (r,c) in visited:
                return
            if (r,c) in all_visited:
                return
            
            visited.add((r,c))
            dfs(r+1, c, visited)
            dfs(r-1, c, visited)
            dfs(r, c+1, visited)
            dfs(r, c-1, visited)
        
        islands = []
        areas = []
        all_visited = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r,c) not in all_visited:
                    visited = set()
                    dfs(r, c, visited)
                    islands.append(visited)
                    areas.append(len(visited))

                    all_visited = all_visited | visited
        
        if len(areas) == 0:
            return 0
            
        return max(areas)
                    
