'''
https://leetcode.com/problems/maximum-product-subarray/
DP
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [1, 1]
        res = nums[0]

        for num in nums:
            if num < 0:
                tmp = dp[1]
                dp[1] = dp[0]
                dp[0] = tmp
            
            dp[0] = min(num, num*dp[0])
            dp[1] = max(num, num*dp[1])

            res = max(res, dp[1])
        
        return res