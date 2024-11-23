'''
https://leetcode.com/problems/house-robber/description/
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0,0]

        for num in nums:
            tmp = dp[1]
            dp[1] = max(dp[1], dp[0]+num)
            dp[0] = tmp
        
        return dp[1]
