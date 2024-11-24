'''
https://leetcode.com/problems/unique-paths-ii/
DP
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dp():
            m, n = len(obstacleGrid), len(obstacleGrid[0])

            if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
                return 0

            prevRow = [0] * n

            for r in range(m-1, -1, -1):
                currRow = [0] * n
                for c in range(n-1, -1, -1):
                    if obstacleGrid[r][c] == 1:
                        currRow[c] = 0
                    else:
                        if c == n-1:
                            currRow[c] = prevRow[c]
                        else:
                            currRow[c] = prevRow[c] + currRow[c+1]
                        if r == m-1 and c == n-1:
                            currRow[c] = 1
                prevRow = currRow

            return currRow[0]
        
        return dp()