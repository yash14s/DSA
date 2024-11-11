'''
https://leetcode.com/problems/combination-sum/
Backtracking, also see subsets.py
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, total):
            if total == target:
                res.append(path.copy())
                return 
            if total > target or i >= len(candidates):
                return
            
            path.append(candidates[i])
            total += candidates[i]
            dfs(i, total)
            path.pop()
            total -= candidates[i]
            dfs(i+1, total)
        
        dfs(0, 0)
        return res