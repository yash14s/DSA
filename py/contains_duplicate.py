'''
https://leetcode.com/problems/contains-duplicate/
Sets
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = set()
        for num in nums:
            if num not in counts:
                counts.add(num)
            else:
                return True
        return False