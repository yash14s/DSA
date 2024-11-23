'''
https://leetcode.com/problems/climbing-stairs/
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        def recursion(n):
            #Exceeds time limit for large n
            if n == 1:
                return 1
            if n == 2:
                return 2
            return recursion(n-1) + recursion(n-2)

        def memoization(n, cache):
            if n == 1:
                return 1
            if n == 2:
                return 2

            if n in cache:
                return cache[n]
            
            cache[n] = memoization(n-1, cache) + memoization(n-2, cache)
            return cache[n]

        #return memoization(n, {})

        def dpBottomUp(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            dp = [1, 2]
            i = 3

            while i <= n:
                tmp = dp[1]
                dp[1] = dp[1] + dp[0]
                dp[0] = tmp
                i += 1
            
            return dp[1]
            
        return dpBottomUp(n)