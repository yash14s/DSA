'''
https://leetcode.com/problems/unique-paths/
DP
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp():
            prevRow = [0] * n

            for r in range(m-1, -1, -1):
                currRow = [0] * n
                currRow[n-1] = 1
                for c in range(n-2, -1, -1):
                    currRow[c] = prevRow[c] + currRow[c+1]
                prevRow = currRow
            
            return currRow[0]

        return dp()