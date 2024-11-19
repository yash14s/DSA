'''
https://leetcode.com/problems/number-of-islands/
Matrix DFS
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c, visited):
            if min(r,c) < 0 or r >= m or c >= n:
                return
            if grid[r][c] == '0':
                return
            if (r,c) in visited:
                return
            
            visited.add((r,c))
            dfs(r+1, c, visited)
            dfs(r-1, c, visited)
            dfs(r, c+1, visited)
            dfs(r, c-1, visited)
        
        count = 0
        visited = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count +=1 
                    dfs(r, c, visited)

        return count