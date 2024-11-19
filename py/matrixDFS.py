'''
https://neetcode.io/problems/matrixDFS
'''

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c, visit):
            if min(r,c) < 0 or r == m or c == n:
                return 0
            if grid[r][c] == 1:
                return 0
            if (r, c) in visit:
                return 0
            if r == m-1 and c == n-1:
                return 1
            
            count = 0
            visit.add((r,c))

            count += dfs(r+1, c, visit)
            count += dfs(r-1, c, visit)
            count += dfs(r, c+1, visit)
            count += dfs(r, c-1, visit)
            
            visit.remove((r,c))

            return count

        return dfs(0,0,set())