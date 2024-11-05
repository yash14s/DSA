'''
https://leetcode.com/problems/first-bad-version/

binary search
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def find_bad_version_recursive(self, l, r):
        if l > r:
            return l

        mid = (l+r)//2

        if isBadVersion(mid):
            return self.find_bad_version_recursive(l, mid-1)
        
        else:
            return self.find_bad_version_recursive(mid+1, r)


    def firstBadVersion(self, n: int) -> int:
        return self.find_bad_version_recursive(1,n)
        