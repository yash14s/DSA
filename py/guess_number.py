'''
https://leetcode.com/problems/guess-number-higher-or-lower/description/
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:

    def guess_recursive(self, l, r):
        mid = (l+r)//2
        
        if guess(mid) == 0:
            return mid
        
        elif guess(mid) == -1:
            return self.guess_recursive(l, mid-1)
        
        else:
            return self.guess_recursive(mid+1, r)


    def guessNumber(self, n: int) -> int:
        
        return self.guess_recursive(1,n)
        