'''
https://leetcode.com/problems/reverse-bits/
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        bitsRemaining = 32

        while n > 0:
            lastDigit = n & 1
            ans += lastDigit * 2**(bitsRemaining-1)
            n = n >> 1
            bitsRemaining -= 1
            
        return ans